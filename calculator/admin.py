from django.contrib import admin
from calculator.sourcemodels.profnastil import *
from calculator.sourcemodels.rabiza import *
from calculator.sourcemodels.metal import *
from calculator.sourcemodels.boarder import *
from calculator.sourcemodels.navesi import *


# profnastil
admin.site.register(Profnastildlinastolbov, ProfnastildlinastolbovAdmin)
admin.site.register(Profnastilystanovkavorot, ProfnastilystanovkavorotAdmin)
admin.site.register(Profnastilystanovkazabora, ProfnastilystanovkazaboraAdmin)
admin.site.register(Profnastilvorota, ProfnastilvorotaAdmin)
admin.site.register(Profnastilkalitka, ProfnastilkalitkaAdmin)
admin.site.register(Profnastilystanovkakalitki, ProfnastilystanovkakalitkiAdmin)
admin.site.register(Profnastilpokraska, ProfnastilpokraskaAdmin)
admin.site.register(Profnastillags, ProfnastillagsAdmin)
admin.site.register(Profnastilshtaketnik, ProfnastilshtaketnikAdmin)


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



# metal
admin.site.register(Metaldlinastolbov, MetaldlinastolbovAdmin)
admin.site.register(Metalystanovkavorot, MetalystanovkavorotAdmin)
admin.site.register(Metalystanovkazabora, MetalystanovkazaboraAdmin)
admin.site.register(Metalvorota, MetalvorotaAdmin)
admin.site.register(Metalkalitka, MetalkalitkaAdmin)
admin.site.register(Metalystanovkakalitki, MetalystanovkakalitkiAdmin)
admin.site.register(Metalpokraska, MetalpokraskaAdmin)
admin.site.register(Metallags, MetallagsAdmin)
admin.site.register(Metalshtaketnik, MetalshtaketnikAdmin)

# boarder
admin.site.register(Boarderkalitka, BoarderkalitkaAdmin)
admin.site.register(Boarderdlinastolbov, BoarderdlinastolbovAdmin)
admin.site.register(Boarderystanovkavorot, BoarderystanovkavorotAdmin)
admin.site.register(Boarderystanovkazabora, BoarderystanovkazaboraAdmin)
admin.site.register(Boardervorota, BoardervorotaAdmin)
admin.site.register(Boarderystanovkakalitki, BoarderystanovkakalitkiAdmin)
admin.site.register(Boarderpokraska, BoarderpokraskaAdmin)
admin.site.register(Boarder3d, Boarder3dAdmin)


# navesi
admin.site.register(Navesidlinastolbov, NavesidlinastolbovAdmin)
admin.site.register(Navesibalka, NavesibalkaAdmin)
admin.site.register(Navesifermi, NavesifermiAdmin)
admin.site.register(Navesiobrfermi, NavesiobrfermiAdmin)
admin.site.register(Navesikrov, NavesikrovAdmin)
admin.site.register(Navesikonek, NavesikonekAdmin)
admin.site.register(Navesibokferma, NavesibokfermaAdmin)
admin.site.register(Navesiveter, NavesiveterAdmin)
admin.site.register(Navesikraska, NavesikraskaAdmin)
admin.site.register(Navesiystanovka, NavesiystanovkaAdmin)
