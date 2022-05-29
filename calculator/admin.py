from django.contrib import admin
from calculator.sourcemodels.profnastil import *
from calculator.sourcemodels.rabiza import *


# profnastil
admin.site.register(ProfnastilSechenieStolba)
admin.site.register(ProfnastilTipStolba)
admin.site.register(ProfnastilTolshinaStolba)
admin.site.register(ProfnastilEdinicaIzmereniya)
admin.site.register(ProfnastilStolba, StolbaAdmin)
admin.site.register(ProfnastilPokritie, PokritieAdmin)
admin.site.register(ProfnastilKraska, KraskaAdmin)
admin.site.register(ProfnastilServicesAndMaterials, ServicesAndMaterialsAdmin)
admin.site.register(ProfnastilLaborCost, LaborCostAdmin)

# rabiza
admin.site.register(Rabizadlinastolbov, RabizadlinastolbovAdmin)
admin.site.register(Rabizasetka, RabizasetkaAdmin)
admin.site.register(Rabizaystanovkavorot, RabizaystanovkavorotAdmin)
admin.site.register(Rabizaystanovkazabora, RabizaystanovkazaboraAdmin)
admin.site.register(Rabizavorota, RabizavorotaAdmin)
admin.site.register(Rabizakalitka, RabizakalitkaAdmin)
admin.site.register(Rabizaystanovkakalitki, RabizaystanovkakalitkiAdmin)
admin.site.register(Rabizapokraska, RabizapokraskaAdmin)
admin.site.register(Rabizaarmatura, RabizaarmaturaAdmin)



# boarder