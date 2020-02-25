from nlp_models.huggingface_wrappers import GenericHuggingfaceWrapper, HuggingfaceModelNames
import numpy as np

hf_model = GenericHuggingfaceWrapper(HuggingfaceModelNames.XLM_ROBERTA_LARGE.value, "cuda", token_limit=200)
hf_model.sentences_forward(np.array([['List', 'of', 'genera', 'This', 'is', 'an', 'incomplete', 'list', 'of', 'genera', 'in', 'the', 'Nectriaceae', 'family', ':', 'AcremoniopsisActinostilbeAlbonectriaAllonectellaAllantonectriaAquanectriaAtractiumBaipadisphaeriaCalonectriaCalostilbeCalostilbellaCampylocarponChaetopsinaCoccinonectriaCorallomycesCorallomycetellaCorallonectriaCosmosporaCurvicladiellaCyanonectriaCylindrocarponCylindrocladiellaCylindrocladiumFusariumFusicollaGibberellaGliocephalotrichumGlionectriaHaematonectriaLanatonectriaLeuconectriaNectriaNectricladiellaNeocosmosporaNeonectriaOphionectriaPleogibberellaPseudonectriaRubrinectriaStalagmitesTuberculariaTumenectriaVaricosporellopsisViridisporaVolutellaXenoacremoniumXenocalonectriaXenocylindrocladiumXenogliocladiopsisXenoleptographiumXenonectriellaZythiostroma', 'References', 'External', 'links', 'Nectriaceae', 'in', 'Index', 'Fungorum']]))