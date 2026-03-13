from django.contrib import admin
from user_service.models import (
    UserProfile, Permission, Role,
    UserVerification, Documents, OwnerDocuments,
    TenantDocuments, \
        FAQ, PrivacyPolicy
)
from property_management.models import (
    LeasePropertyDetails, UserInvitation, Template, TemplateFields,
    TemplateValues,LeaseDocumentsMapping , TermAndCondition ,AuditLog , Approval
)


# -------------------- User Service Admin --------------------
class CompanyStaffAdmin(admin.ModelAdmin):
    list_display = ["id", "staff", "company", "is_active"]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "contact_number"]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ["id", "module_name"]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "company"]


@admin.register(UserVerification)
class UserVerificationAdmin(admin.ModelAdmin):
    list_display = ["id", "verification_type", "otp", "is_verified"]


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ["id", "file_name"]


@admin.register(OwnerDocuments)
class OwnerDocumentsAdmin(admin.ModelAdmin):
    list_display = ["id", "owner"]


@admin.register(TenantDocuments)
class TenantDocumentsAdmin(admin.ModelAdmin):
    list_display = ["id", "tenant"]



@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "question")



# -------------------- Property Management Admin --------------------
@admin.register(LeasePropertyDetails)
class LeasePropertyDetailsAdmin(admin.ModelAdmin):
    list_display = ["id", "lease_property", "tenant", "owner", "lease_status", "lease_start_date", "lease_end_date"]


@admin.register(UserInvitation)
class UserInvitationAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "invited_by", "invitation_type", "status"]


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "template_path", "is_active"]


@admin.register(TemplateFields)
class TemplateFieldsAdmin(admin.ModelAdmin):
    list_display = ["id", "document_template", "name_attribute", "label_attribute", "html_tag"]


@admin.register(TemplateValues)
class TemplateValuesAdmin(admin.ModelAdmin):
    list_display = ["id", "document_template", "lease"]


@admin.register(LeaseDocumentsMapping)
class LeaseDocumentsMappingAdmin(admin.ModelAdmin):
    list_display = ("id", "lease", "document", "document_choice")


@admin.register(TermAndCondition)
class TermAndConditionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "term_type",
        "lease",
        "is_predefined",
    )

admin.site.register(CompanyStaff, CompanyStaffAdmin)

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("lead_id", "name", "get_tenant", "unit", "email", "contact_number", "status", "platform", "lead_type")
    search_fields = ("lead_id", "name", "email", "contact_number")
    list_filter = ("status", "platform", "lead_type")

    def get_tenant(self, obj):
        if obj.tenant:
            return f"{obj.tenant.user.first_name} {obj.tenant.user.last_name}".strip()
        return "-"
    get_tenant.short_description = "Tenant"

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ["id","userprofile","action_type","message","created"]
    list_filter = ["action_type","created"]
    search_fields = ["message","userprofile__user__username"]


@admin.register(UnitDetails)
class UnitDetailsAdmin(admin.ModelAdmin):
    list_display = ["id", "unit_name", "property", "property_block_tower", "property_type", "floor_no", "no_of_bedrooms", "is_occupied", "company"]
    search_fields = ["unit_name", "plot_no", "makani_no", "dewa_no"]
    list_filter = ["property_type", "is_occupied", "step_status"]

@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ["date_requested","requested_by","property_unit","tenant","tenure","rent","actual_rent","is_approved","is_rejected"]
    list_filter = ["is_approved","is_rejected","date_requested"]
