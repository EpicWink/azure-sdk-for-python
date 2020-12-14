# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class DataDestinationType(str, Enum):

    storage_account = "StorageAccount"  #: Storage Accounts .
    managed_disk = "ManagedDisk"  #: Azure Managed disk storage.


class ShareDestinationFormatType(str, Enum):

    unknown_type = "UnknownType"  #: Unknown format.
    hcs = "HCS"  #: Storsimple data format.
    block_blob = "BlockBlob"  #: Azure storage block blob format.
    page_blob = "PageBlob"  #: Azure storage page blob format.
    azure_file = "AzureFile"  #: Azure storage file format.
    managed_disk = "ManagedDisk"  #: Azure Compute Disk.


class AccessProtocol(str, Enum):

    smb = "SMB"  #: Server Message Block protocol(SMB).
    nfs = "NFS"  #: Network File System protocol(NFS).


class AddressValidationStatus(str, Enum):

    valid = "Valid"  #: Address provided is valid.
    invalid = "Invalid"  #: Address provided is invalid or not supported.
    ambiguous = "Ambiguous"  #: Address provided is ambiguous, please choose one of the alternate addresses returned.


class AddressType(str, Enum):

    none = "None"  #: Address type not known.
    residential = "Residential"  #: Residential Address.
    commercial = "Commercial"  #: Commercial Address.


class SkuName(str, Enum):

    data_box = "DataBox"  #: Databox.
    data_box_disk = "DataBoxDisk"  #: DataboxDisk.
    data_box_heavy = "DataBoxHeavy"  #: DataboxHeavy.


class SkuDisabledReason(str, Enum):

    none = "None"  #: SKU is not disabled.
    country = "Country"  #: SKU is not available in the requested country.
    region = "Region"  #: SKU is not available to push data to the requested Azure region.
    feature = "Feature"  #: Required features are not enabled for the SKU.
    offer_type = "OfferType"  #: Subscription does not have required offer types for the SKU.
    no_subscription_info = "NoSubscriptionInfo"  #: Subscription has not registered to Microsoft.DataBox and Service does not have the subscription notification.


class NotificationStageName(str, Enum):

    device_prepared = "DevicePrepared"  #: Notification at device prepared stage.
    dispatched = "Dispatched"  #: Notification at device dispatched stage.
    delivered = "Delivered"  #: Notification at device delivered stage.
    picked_up = "PickedUp"  #: Notification at device picked up from user stage.
    at_azure_dc = "AtAzureDC"  #: Notification at device received at azure datacenter stage.
    data_copy = "DataCopy"  #: Notification at data copy started stage.


class ValidationStatus(str, Enum):

    valid = "Valid"  #: Validation is successful
    invalid = "Invalid"  #: Validation is not successful
    skipped = "Skipped"  #: Validation is skipped


class CopyStatus(str, Enum):

    not_started = "NotStarted"  #: Data copy hasn't started yet.
    in_progress = "InProgress"  #: Data copy is in progress.
    completed = "Completed"  #: Data copy completed.
    completed_with_errors = "CompletedWithErrors"  #: Data copy completed with errors.
    failed = "Failed"  #: Data copy failed. No data was copied.
    not_returned = "NotReturned"  #: No copy triggered as device was not returned.
    hardware_error = "HardwareError"  #: The Device has hit hardware issues.
    device_formatted = "DeviceFormatted"  #: Data copy failed. The Device was formatted by user.
    device_metadata_modified = "DeviceMetadataModified"  #: Data copy failed. Device metadata was modified by user.
    storage_account_not_accessible = "StorageAccountNotAccessible"  #: Data copy failed. Storage Account was not accessible during copy.
    unsupported_data = "UnsupportedData"  #: Data copy failed. The Device data content is not supported.


class StageName(str, Enum):

    device_ordered = "DeviceOrdered"  #: An order has been created.
    device_prepared = "DevicePrepared"  #: A device has been prepared for the order.
    dispatched = "Dispatched"  #: Device has been dispatched to the user of the order.
    delivered = "Delivered"  #: Device has been delivered to the user of the order.
    picked_up = "PickedUp"  #: Device has been picked up from user and in transit to azure datacenter.
    at_azure_dc = "AtAzureDC"  #: Device has been received at azure datacenter from the user.
    data_copy = "DataCopy"  #: Data copy from the device at azure datacenter.
    completed = "Completed"  #: Order has completed.
    completed_with_errors = "CompletedWithErrors"  #: Order has completed with errors.
    cancelled = "Cancelled"  #: Order has been cancelled.
    failed_issue_reported_at_customer = "Failed_IssueReportedAtCustomer"  #: Order has failed due to issue reported by user.
    failed_issue_detected_at_azure_dc = "Failed_IssueDetectedAtAzureDC"  #: Order has failed due to issue detected at azure datacenter.
    aborted = "Aborted"  #: Order has been aborted.
    completed_with_warnings = "CompletedWithWarnings"  #: Order has completed with warnings.
    ready_to_dispatch_from_azure_dc = "ReadyToDispatchFromAzureDC"  #: Device is ready to be handed to customer from Azure DC.
    ready_to_receive_at_azure_dc = "ReadyToReceiveAtAzureDC"  #: Device can be dropped off at Azure DC.


class StageStatus(str, Enum):

    none = "None"  #: No status available yet.
    in_progress = "InProgress"  #: Stage is in progress.
    succeeded = "Succeeded"  #: Stage has succeeded.
    failed = "Failed"  #: Stage has failed.
    cancelled = "Cancelled"  #: Stage has been cancelled.
    cancelling = "Cancelling"  #: Stage is cancelling.
    succeeded_with_errors = "SucceededWithErrors"  #: Stage has succeeded with errors.


class TransportShipmentTypes(str, Enum):

    customer_managed = "CustomerManaged"  #: Shipment Logistics is handled by the customer.
    microsoft_managed = "MicrosoftManaged"  #: Shipment Logistics is handled by Microsoft.


class JobDeliveryType(str, Enum):

    non_scheduled = "NonScheduled"  #: Non Scheduled job.
    scheduled = "Scheduled"  #: Scheduled job.


class OverallValidationStatus(str, Enum):

    all_valid_to_proceed = "AllValidToProceed"  #: Every input request is valid.
    inputs_revisit_required = "InputsRevisitRequired"  #: Some input requests are not valid.
    certain_input_validations_skipped = "CertainInputValidationsSkipped"  #: Certain input validations skipped.