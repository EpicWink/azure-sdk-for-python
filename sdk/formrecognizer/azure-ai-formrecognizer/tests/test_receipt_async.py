# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
import functools
from io import BytesIO
from datetime import date, time
from azure.core.exceptions import ServiceRequestError, ClientAuthenticationError, HttpResponseError
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer._generated.models import AnalyzeOperationResult
from azure.ai.formrecognizer._response_handlers import prepare_prebuilt_models
from azure.ai.formrecognizer.aio import FormRecognizerClient
from azure.ai.formrecognizer import FormContentType, FormRecognizerApiVersion
from preparers import FormRecognizerPreparer
from asynctestcase import AsyncFormRecognizerTest
from preparers import GlobalClientPreparer as _GlobalClientPreparer


GlobalClientPreparer = functools.partial(_GlobalClientPreparer, FormRecognizerClient)


class TestReceiptFromStreamAsync(AsyncFormRecognizerTest):

    @FormRecognizerPreparer()
    async def test_receipt_bad_endpoint(self, formrecognizer_test_endpoint, formrecognizer_test_api_key):
        with open(self.receipt_jpg, "rb") as fd:
            myfile = fd.read()
        with self.assertRaises(ServiceRequestError):
            client = FormRecognizerClient("http://notreal.azure.com", AzureKeyCredential(formrecognizer_test_api_key))
            async with client:
                poller = await client.begin_recognize_receipts(myfile)
                result = await poller.result()

    @FormRecognizerPreparer()
    async def test_authentication_bad_key(self, formrecognizer_test_endpoint, formrecognizer_test_api_key):
        client = FormRecognizerClient(formrecognizer_test_endpoint, AzureKeyCredential("xxxx"))
        with self.assertRaises(ClientAuthenticationError):
            async with client:
                poller = await client.begin_recognize_receipts(b"xx", content_type="image/jpeg")
                result = await poller.result()

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_passing_enum_content_type(self, client):
        with open(self.receipt_png, "rb") as fd:
            myfile = fd.read()
        async with client:
            poller = await client.begin_recognize_receipts(
                myfile,
                content_type=FormContentType.IMAGE_PNG
            )
            result = await poller.result()
        self.assertIsNotNone(result)

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_damaged_file_passed_as_bytes(self, client):
        damaged_pdf = b"\x25\x50\x44\x46\x55\x55\x55"  # still has correct bytes to be recognized as PDF
        with self.assertRaises(HttpResponseError):
            async with client:
                poller = await client.begin_recognize_receipts(
                    damaged_pdf,
                )
                result = await poller.result()

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_damaged_file_bytes_fails_autodetect_content_type(self, client):
        damaged_pdf = b"\x50\x44\x46\x55\x55\x55"  # doesn't match any magic file numbers
        with self.assertRaises(ValueError):
            async with client:
                poller = await client.begin_recognize_receipts(
                    damaged_pdf,
                )
                result = await poller.result()

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_damaged_file_passed_as_bytes_io(self, client):
        damaged_pdf = BytesIO(b"\x25\x50\x44\x46\x55\x55\x55")  # still has correct bytes to be recognized as PDF
        with self.assertRaises(HttpResponseError):
            async with client:
                poller = await client.begin_recognize_receipts(
                    damaged_pdf,
                )
                result = await poller.result()

    @FormRecognizerPreparer()
    async def test_damaged_file_bytes_io_fails_autodetect(self, formrecognizer_test_endpoint, formrecognizer_test_api_key):
        client = FormRecognizerClient(formrecognizer_test_endpoint, AzureKeyCredential(formrecognizer_test_api_key))
        damaged_pdf = BytesIO(b"\x50\x44\x46\x55\x55\x55")  # doesn't match any magic file numbers
        with self.assertRaises(ValueError):
            async with client:
                poller = await client.begin_recognize_receipts(
                    damaged_pdf,
                )
                result = await poller.result()

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_blank_page(self, client):

        with open(self.blank_pdf, "rb") as fd:
            blank = fd.read()
        async with client:
            poller = await client.begin_recognize_receipts(
                blank,
            )
            result = await poller.result()
        self.assertIsNotNone(result)

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_passing_bad_content_type_param_passed(self, client):
        with open(self.receipt_jpg, "rb") as fd:
            myfile = fd.read()
        with self.assertRaises(ValueError):
            async with client:
                poller = await client.begin_recognize_receipts(
                    myfile,
                    content_type="application/jpeg"
                )
                result = await poller.result()

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_passing_unsupported_url_content_type(self, client):
        with self.assertRaises(TypeError):
            async with client:
                poller = await client.begin_recognize_receipts("https://badurl.jpg", content_type="application/json")
                result = await poller.result()

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_auto_detect_unsupported_stream_content(self, client):
        with open(self.unsupported_content_py, "rb") as fd:
            myfile = fd.read()

        with self.assertRaises(ValueError):
            async with client:
                poller = await client.begin_recognize_receipts(
                    myfile,
                )
                result = await poller.result()

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_receipt_stream_transform_png(self, client):

        responses = []

        def callback(raw_response, _, headers):
            analyze_result = client._deserialize(AnalyzeOperationResult, raw_response)
            extracted_receipt = prepare_prebuilt_models(analyze_result)
            responses.append(analyze_result)
            responses.append(extracted_receipt)

        with open(self.receipt_png, "rb") as fd:
            myfile = fd.read()

        async with client:
            poller = await client.begin_recognize_receipts(
                receipt=myfile,
                include_field_elements=True,
                cls=callback
            )
            result = await poller.result()

        raw_response = responses[0]
        returned_model = responses[1]
        receipt = returned_model[0]
        actual = raw_response.analyze_result.document_results[0].fields
        read_results = raw_response.analyze_result.read_results
        document_results = raw_response.analyze_result.document_results

        # check dict values
        self.assertFormFieldsTransformCorrect(receipt.fields, actual, read_results)

        # check page range
        self.assertEqual(receipt.page_range.first_page_number, document_results[0].page_range[0])
        self.assertEqual(receipt.page_range.last_page_number, document_results[0].page_range[1])

        # Check page metadata
        self.assertFormPagesTransformCorrect(receipt.pages, read_results)

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_receipt_stream_transform_jpg(self, client):
        responses = []

        def callback(raw_response, _, headers):
            analyze_result = client._deserialize(AnalyzeOperationResult, raw_response)
            extracted_receipt = prepare_prebuilt_models(analyze_result)
            responses.append(analyze_result)
            responses.append(extracted_receipt)

        with open(self.receipt_jpg, "rb") as fd:
            myfile = fd.read()

        async with client:
            poller = await client.begin_recognize_receipts(
                receipt=myfile,
                include_field_elements=True,
                cls=callback
            )
            result = await poller.result()

        raw_response = responses[0]
        returned_model = responses[1]
        receipt = returned_model[0]
        actual = raw_response.analyze_result.document_results[0].fields
        read_results = raw_response.analyze_result.read_results
        document_results = raw_response.analyze_result.document_results
        page_results = raw_response.analyze_result.page_results

        # check dict values
        self.assertFormFieldsTransformCorrect(receipt.fields, actual, read_results)

        # check page range
        self.assertEqual(receipt.page_range.first_page_number, document_results[0].page_range[0])
        self.assertEqual(receipt.page_range.last_page_number, document_results[0].page_range[1])

        # Check form pages
        self.assertFormPagesTransformCorrect(receipt.pages, read_results)

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_receipt_png(self, client):
        with open(self.receipt_png, "rb") as fd:
            receipt = fd.read()

        async with client:
            poller = await client.begin_recognize_receipts(receipt)
            result = await poller.result()
        self.assertEqual(len(result), 1)
        receipt = result[0]
        self.assertEqual(receipt.fields.get("MerchantAddress").value, '123 Main Street Redmond, WA 98052')
        self.assertEqual(receipt.fields.get("MerchantName").value, 'Contoso')
        self.assertEqual(receipt.fields.get("Subtotal").value, 1098.99)
        self.assertEqual(receipt.fields.get("Tax").value, 104.4)
        self.assertEqual(receipt.fields.get("Total").value, 1203.39)
        self.assertEqual(receipt.fields.get("TransactionDate").value, date(year=2019, month=6, day=10))
        self.assertEqual(receipt.fields.get("TransactionTime").value, time(hour=13, minute=59, second=0))
        self.assertEqual(receipt.page_range.first_page_number, 1)
        self.assertEqual(receipt.page_range.last_page_number, 1)
        self.assertFormPagesHasValues(receipt.pages)
        receipt_type = receipt.fields.get("ReceiptType")
        self.assertIsNotNone(receipt_type.confidence)
        self.assertEqual(receipt_type.value, 'Itemized')

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_receipt_jpg_include_field_elements(self, client):
        with open(self.receipt_jpg, "rb") as fd:
            receipt = fd.read()
        async with client:
            poller = await client.begin_recognize_receipts(receipt, include_field_elements=True)
            result = await poller.result()

        self.assertEqual(len(result), 1)
        receipt = result[0]

        self.assertFormPagesHasValues(receipt.pages)

        for name, field in receipt.fields.items():
            if field.value_type not in ["list", "dictionary"] and name != "ReceiptType":  # receipt cases where value_data is None
                self.assertFieldElementsHasValues(field.value_data.field_elements, receipt.page_range.first_page_number)

        self.assertEqual(receipt.fields.get("MerchantAddress").value, '123 Main Street Redmond, WA 98052')
        self.assertEqual(receipt.fields.get("MerchantName").value, 'Contoso')
        self.assertEqual(receipt.fields.get("MerchantPhoneNumber").value, '+19876543210')
        self.assertEqual(receipt.fields.get("Subtotal").value, 11.7)
        self.assertEqual(receipt.fields.get("Tax").value, 1.17)
        self.assertEqual(receipt.fields.get("Tip").value, 1.63)
        self.assertEqual(receipt.fields.get("Total").value, 14.5)
        self.assertEqual(receipt.fields.get("TransactionDate").value, date(year=2019, month=6, day=10))
        self.assertEqual(receipt.fields.get("TransactionTime").value, time(hour=13, minute=59, second=0))
        self.assertEqual(receipt.page_range.first_page_number, 1)
        self.assertEqual(receipt.page_range.last_page_number, 1)
        self.assertFormPagesHasValues(receipt.pages)
        receipt_type = receipt.fields.get("ReceiptType")
        self.assertIsNotNone(receipt_type.confidence)
        self.assertEqual(receipt_type.value, 'Itemized')

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_receipt_multipage(self, client):
        with open(self.multipage_receipt_pdf, "rb") as fd:
            receipt = fd.read()
        async with client:
            poller = await client.begin_recognize_receipts(receipt, include_field_elements=True)
            result = await poller.result()

        self.assertEqual(len(result), 2)
        receipt = result[0]
        self.assertEqual(receipt.fields.get("MerchantAddress").value, '123 Main Street Redmond, WA 98052')
        self.assertEqual(receipt.fields.get("MerchantName").value, 'Contoso')
        self.assertEqual(receipt.fields.get("MerchantPhoneNumber").value, '+19876543210')
        self.assertEqual(receipt.fields.get("Subtotal").value, 11.7)
        self.assertEqual(receipt.fields.get("Tax").value, 1.17)
        self.assertEqual(receipt.fields.get("Tip").value, 1.623)
        self.assertEqual(receipt.fields.get("Total").value, 14.52)
        self.assertEqual(receipt.fields.get("TransactionDate").value, date(year=2019, month=6, day=10))
        self.assertEqual(receipt.fields.get("TransactionTime").value, time(hour=13, minute=59, second=0))
        self.assertEqual(receipt.page_range.first_page_number, 1)
        self.assertEqual(receipt.page_range.last_page_number, 1)
        self.assertFormPagesHasValues(receipt.pages)
        receipt_type = receipt.fields.get("ReceiptType")
        self.assertIsNotNone(receipt_type.confidence)
        self.assertEqual(receipt_type.value, 'Itemized')
        receipt = result[1]
        self.assertEqual(receipt.fields.get("MerchantAddress").value, '123 Main Street Redmond, WA 98052')
        self.assertEqual(receipt.fields.get("MerchantName").value, 'Contoso')
        self.assertEqual(receipt.fields.get("Subtotal").value, 1098.99)
        self.assertEqual(receipt.fields.get("Tax").value, 104.4)
        self.assertEqual(receipt.fields.get("Total").value, 1203.39)
        self.assertEqual(receipt.fields.get("TransactionDate").value, date(year=2019, month=6, day=10))
        self.assertEqual(receipt.fields.get("TransactionTime").value, time(hour=13, minute=59, second=0))
        self.assertEqual(receipt.page_range.first_page_number, 2)
        self.assertEqual(receipt.page_range.last_page_number, 2)
        self.assertFormPagesHasValues(receipt.pages)
        receipt_type = receipt.fields.get("ReceiptType")
        self.assertIsNotNone(receipt_type.confidence)
        self.assertEqual(receipt_type.value, 'Itemized')

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_receipt_multipage_transform(self, client):
        responses = []

        def callback(raw_response, _, headers):
            analyze_result = client._deserialize(AnalyzeOperationResult, raw_response)
            extracted_receipt = prepare_prebuilt_models(analyze_result)
            responses.append(analyze_result)
            responses.append(extracted_receipt)

        with open(self.multipage_receipt_pdf, "rb") as fd:
            myfile = fd.read()

        async with client:
            poller = await client.begin_recognize_receipts(
                receipt=myfile,
                include_field_elements=True,
                cls=callback
            )
            result = await poller.result()

        raw_response = responses[0]
        returned_model = responses[1]
        actual = raw_response.analyze_result.document_results
        read_results = raw_response.analyze_result.read_results
        document_results = raw_response.analyze_result.document_results
        page_results = raw_response.analyze_result.page_results

        # check hardcoded values
        for receipt, actual in zip(returned_model, actual):

            # check dict values
            self.assertFormFieldsTransformCorrect(receipt.fields, actual.fields, read_results)

            # check page range
            self.assertEqual(receipt.page_range.first_page_number, actual.page_range[0])
            self.assertEqual(receipt.page_range.last_page_number, actual.page_range[1])

        # Check form pages
        self.assertFormPagesTransformCorrect(returned_model, read_results)

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    @pytest.mark.live_test_only
    async def test_receipt_continuation_token(self, client):

        with open(self.receipt_jpg, "rb") as fd:
            receipt = fd.read()

        async with client:
            initial_poller = await client.begin_recognize_receipts(receipt)
            cont_token = initial_poller.continuation_token()
            poller = await client.begin_recognize_receipts(None, continuation_token=cont_token)
            result = await poller.result()
            self.assertIsNotNone(result)
            await initial_poller.wait()  # necessary so azure-devtools doesn't throw assertion error

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_receipt_locale_specified(self, client):
        with open(self.receipt_jpg, "rb") as fd:
            receipt = fd.read()
        async with client:
            poller = await client.begin_recognize_receipts(receipt, locale="en-IN")
            assert 'en-IN' == poller._polling_method._initial_response.http_response.request.query['locale']
            result = await poller.result()
            assert result

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_receipt_locale_error(self, client):
        with open(self.receipt_jpg, "rb") as fd:
            receipt = fd.read()
        with pytest.raises(HttpResponseError) as e:
            async with client:
                await client.begin_recognize_receipts(receipt, locale="not a locale")
        assert "UnsupportedLocale" == e.value.error.code

    @FormRecognizerPreparer()
    @GlobalClientPreparer(client_kwargs={"api_version": FormRecognizerApiVersion.V2_0})
    async def test_receipt_locale_v2(self, client):
        with open(self.receipt_jpg, "rb") as fd:
            receipt = fd.read()
        with pytest.raises(ValueError) as e:
            async with client:
                await client.begin_recognize_receipts(receipt, locale="en-US")
        assert "'locale' is only available for API version V2_1 and up" in str(e.value)

    @FormRecognizerPreparer()
    @GlobalClientPreparer()
    async def test_pages_kwarg_specified(self, client):
        with open(self.receipt_jpg, "rb") as fd:
            receipt = fd.read()
        async with client:
            poller = await client.begin_recognize_receipts(receipt, pages=["1"])
            assert '1' == poller._polling_method._initial_response.http_response.request.query['pages']
            result = await poller.result()
            assert result
