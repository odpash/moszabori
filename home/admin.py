from django.contrib import admin
from home.models import *
# (
#                         Page, 
#                         # ServiceList, 
#                         SEO_Optimiser,
#                         # HowDoesItWork, 
#                         FAQ,
#                         Pricelist, PricelistCategory,
#                         ServiceCategory, Services,

#                         )
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('Title', 'pageid',  'SEO', 'template' )
    list_filter =  [
        'Title', 
        'Created', 
        'Updated',
    ]
    # list_editable = ['Price', 'Available' ]
    # prepopulated_fields = {'Slug':('Title',) }
admin.site.register(Page, PageAdmin)

class SEOAdmin(admin.ModelAdmin):
    list_display = ( 'PageName','Title', 'id', 'seoid', 'Image' )
    list_filter =  ['PageName', 'Title', ]
    save_as = True
    # readonly_fields = ("PageName", 'id')
admin.site.register(SEO_Optimiser, SEOAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display = ('Title', 'id', )
    list_filter =  ['Title', ]
admin.site.register(FAQ, FAQAdmin)

admin.site.register(PricelistCategory)

class PricelistAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Category', )
    list_filter =  ['Title', 'Category', ]
admin.site.register(Pricelist, PricelistAdmin)

# This is used for zabor 
# admin.site.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('Title',  )
    # list_filter =  ['Title', 'Category', ]
    prepopulated_fields = {'Slug':('Title',) }
    save_as = True
admin.site.register(ServiceCategory, ServiceCategoryAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('ShortTitle', 'Category', )
    list_filter =  ['Title', 'Category', ]
    prepopulated_fields = {'Slug':('Title',) }
    save_as = True
admin.site.register(Services, ServicesAdmin)


# admin.site.register(NavesCategory)
class NavesCategoryAdmin(admin.ModelAdmin):
    list_display = ('Title',  )
    # list_filter =  ['Title', 'Category', ]
    prepopulated_fields = {'Slug':('Title',) }
    save_as = True
admin.site.register(NavesCategory, NavesCategoryAdmin)

class NavesAdmin(admin.ModelAdmin):
    list_display = ('ShortTitle', 'Category', )
    list_filter =  ['Title', 'Category', ]
    prepopulated_fields = {'Slug':('Title',) }
    save_as = True
admin.site.register(Naves, NavesAdmin)

# admin.site.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('Title', )
    list_filter =  ['Title', ]
    prepopulated_fields = {'Slug':('Title',) }
admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('ShortTitle', 'Category', )
    list_filter =  ['Title', 'Category', ]
    prepopulated_fields = {'Slug':('Title',) }
admin.site.register(Portfolio, PortfolioAdmin)
