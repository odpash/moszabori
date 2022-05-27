from django.contrib import admin
from calculator.sourcemodels.profnastil import *
from calculator.sourcemodels.rabiza import *
from calculator.sourcemodels.boarder import *
from calculator.sourcemodels.metal import *
from calculator.sourcemodels.navesi import *
# Register your models here.


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
admin.site.register(Rabizadlinazabora, RabizadlinazaboraAdmin)
admin.site.register(Rabizakmmkad, RabizakmmkadAdmin)
admin.site.register(Rabizavisotazabora, RabizavisotazaboraAdmin)
admin.site.register(Rabizamethodystanovkistolbov, RabizamethodystanovkistolbovAdmin)
admin.site.register(Rabizarazmertolshinastolb, RabizarazmertolshinastolbAdmin)
admin.site.register(Rabizapokraskastolb, RabizapokraskastolbAdmin)
admin.site.register(Rabizaraspashnievorota, RabizaraspashnievorotaAdmin)
admin.site.register(Rabizakalitkastandart, RabizakalitkastandartAdmin)
admin.site.register(Rabizashirinavorot, RabizashirinavorotAdmin)
admin.site.register(Rabizademontashvorot, RabizademontashvorotAdmin)

# boarder
admin.site.register(BoarderdlinaZabora, BoarderdlinaZaboraAdmin)
admin.site.register(BoardervisotaZabora, BoardervisotaZaboraAdmin)
admin.site.register(Boarderpaneli, BoarderpaneliAdmin)
admin.site.register(Boarderrazmer, BoarderrazmerAdmin)
admin.site.register(Boardermethodstand, BoardermethodstandAdmin)
admin.site.register(BoarderkalitkaStandart, BoarderkalitkaStandartAdmin)
admin.site.register(Boarderraspashvorota, BoarderraspashvorotaAdmin)
admin.site.register(Boarderotkat, BoarderotkatAdmin)
admin.site.register(BoarderkmMkad, BoarderkmMkadAdmin)
admin.site.register(Boarderdemontash, BoarderdemontashAdmin)

# metal
admin.site.register(MetaldlinaZabora, MetaldlinaZaboraAdmin)
admin.site.register(MetalvisotaZabora, MetalvisotaZaboraAdmin)
admin.site.register(Metaltipshtaketnik, MetaltipshtaketnikAdmin)
admin.site.register(Metalkreplenieshtaketnik, MetalkreplenieshtaketnikAdmin)
admin.site.register(Metalzazor, MetalzazorAdmin)
admin.site.register(Metalpokritiestaketnik, MetalpokritiestaketnikAdmin)
admin.site.register(Metalkolvoryadlag, MetalkolvoryadlagAdmin)
admin.site.register(Metalmetodystanovki, MetalmetodystanovkiAdmin)
admin.site.register(Metalrazmer, MetalrazmerAdmin)
admin.site.register(Metalshag, MetalshagAdmin)
admin.site.register(Metalpaint, MetalpaintAdmin)
admin.site.register(Metalstandart, MetalstandartAdmin)
admin.site.register(Metalraspash, MetalraspashAdmin)
admin.site.register(Metalotkat, MetalotkatAdmin)
admin.site.register(Metaldetektprotekt, MetaldetektprotektAdmin)
admin.site.register(Metaldemontash, MetaldemontashAdmin)
admin.site.register(MetalkmMkad, MetalkmMkadAdmin)

admin.site.register(NavesidlinaZabora, NavesidlinaZaboraAdmin)
admin.site.register(NavesishirinaZabora, NavesishirinaZaboraAdmin)
admin.site.register(NavesivisotaZabora, NavesivisotaZaboraAdmin)
admin.site.register(Navesityp, NavesitypAdmin)
admin.site.register(Navesirazmer, NavesirazmerAdmin)
admin.site.register(Navesimethod, NavesimethodAdmin)
admin.site.register(Navesikrovlya, NavesikrovlyaAdmin)
admin.site.register(Navesifermi, NavesifermiAdmin)
admin.site.register(NavesikmMkad, NavesikmMkadAdmin)