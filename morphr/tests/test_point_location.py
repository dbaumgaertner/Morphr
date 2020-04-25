from morphr.objectives.point_location import PointLocation
import pytest
import eqlib as eq
from numpy.testing import assert_almost_equal

if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)


DATA = {
    "ref_locations": [[-5.913359216958488, 3.108050813957082, 0.0], [-6.05241561142299, 3.027766513268769, 8.213888137527034e-06], [-6.330525637306414, 2.8671995071385417, -0.02584166134527456], [-6.7369613697638036, 2.6325435700231465, -0.14110785709398277], [-5.787840608115579, 2.890646352252562, 0.0], [-5.9268969446106015, 2.8103620850064024, 8.21386002083427e-06], [-6.20500685140875, 2.6497951475771875, -0.025841639645896454], [-6.611442414432476, 2.4151393082075923, -0.14110773606036797], [-5.536803390496964, 2.4558374288844655, 0.0], [-5.675859611057076, 2.375553228529743, 8.213803787812274e-06], [-5.953969279692275, 2.214986428517099, -0.025841596247956726], [-6.360404503858186, 1.9803307846612714, -0.14110749399761124], [-5.160247563936306, 1.8036240434034463, 0.0], [-5.299303610604895, 1.7233399434048053, 8.213719439351623e-06], [-5.577412922016013, 1.5627733495555975, -0.025841531153239353], [-5.9838476379206, 1.3281179990290706, -0.14110713091549562]],
    "act_locations": [[-5.893714002015976, 3.0672770163682226, -1.0345997039865868], [-6.038328116081858, 2.9671135944731897, -1.0301056523745293], [-6.315441319551463, 2.7672811916471094, -1.0445211074708685], [-6.711022354939664, 2.469132745936724, -1.1401352442088788], [-5.761945573005222, 2.8477023374942716, -1.0026886850856505], [-5.896748485484654, 2.7584385676444394, -0.9932532278562874], [-6.167009459541683, 2.5640282347862096, -0.9978370290890177], [-6.55636240841509, 2.2769722543396016, -1.0601387134380749], [-5.505967727575608, 2.403226547865329, -0.952548449236662], [-5.641518976153392, 2.30919698947417, -0.9389890585147445], [-5.908037268537961, 2.119496685381821, -0.9300917221862073], [-6.305684302307734, 1.8285004705746841, -0.9599110900403799], [-5.158138651014222, 1.7350625616129978, -0.7036400650717224], [-5.294861415334098, 1.641716404275053, -0.6927569013850762], [-5.569378780794629, 1.4417593721067148, -0.6877700953192258], [-5.987039515181131, 1.13894710512742, -0.7131222126712982]],
    "shape_functions": [[0.06296955421979775, 0.024312454313215177, 0.0014530181382256477, 1.868739406033837e-05, 0.4104069535550825, 0.1584575344666592, 0.009470112262315793, 0.00012179594664774567, 0.2160108509120697, 0.08340147884209205, 0.004984435546950607, 6.410526392187337e-05, 0.020099054168618666, 0.0077602159054151855, 0.0004637842943312572, 5.964770596565135e-06]],
    "target": [-5.72437903320755, 2.6668331887137984, -0.9619361778905989],
    "weight": 0.040518243393910705,
    "exp_f": 6.095464742657343e-06,
    "exp_g": [4.4000429342139685e-06, 9.112980822999495e-06, -4.30837132999429e-05, 1.6988502481827788e-06, 3.518508788279189e-06, -1.6634559736476523e-05, 1.0153068846681492e-07, 2.1028140651752714e-07, -9.941537249639383e-07, 1.3057951134139064e-09, 2.704447662266541e-09, -1.2785898486884033e-08, 2.867748134025334e-05, 5.9394269877128e-05, -0.00028080007461305716, 1.1072334297767394e-05, 2.293204217095194e-05, -0.00010841650492470792, 6.617309120621801e-07, 1.3705186976058185e-06, -6.479442433461105e-06, 8.510579455473175e-09, 1.7626361499173735e-08, -8.333267896657298e-08, 1.509391371823264e-05, 3.126118274635321e-05, -0.0001477944331301352, 5.827738376568764e-06, 1.2069897694445265e-05, -5.7063218054261285e-05, 3.482910222430886e-07, 7.213496445327666e-07, -3.41034639243717e-06, 4.479401467267788e-09, 9.277341216903246e-09, -4.386076487355569e-08, 1.4044358797637746e-06, 2.908743716998768e-06, -1.3751755084340983e-05, 5.422506731334236e-07, 1.1230617653975731e-06, -5.309532858491285e-06, 3.240726145445808e-08, 6.7119061467332e-08, -3.1732080395928836e-07, 4.167926395987111e-10, 8.632241522681677e-10, -4.081090766266617e-09],
    "exp_h": [[0.00016066151078753468, 0.0, 0.0, 6.203117823066924e-05, 0.0, 0.0, 3.707253325538521e-06, 0.0, 0.0, 4.767931105143542e-08, 0.0, 0.0, 0.0010471187546558576, 0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 2.4162193336805556e-05, 0.0, 0.0, 3.107520934310918e-07, 0.0, 0.0, 0.0005511334816329829, 0.0, 0.0, 0.00021279184454623816, 0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 1.635591783796321e-07, 0.0, 0.0, 5.1281042849045966e-05, 0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 1.521860949182208e-08, 0.0, 0.0], [0.0, 0.00016066151078753468, 0.0, 0.0, 6.203117823066924e-05, 0.0, 0.0, 3.707253325538521e-06, 0.0, 0.0, 4.767931105143542e-08, 0.0, 0.0, 0.0010471187546558576, 0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 2.4162193336805556e-05, 0.0, 0.0, 3.107520934310918e-07, 0.0, 0.0, 0.0005511334816329829, 0.0, 0.0, 0.00021279184454623816, 0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 1.635591783796321e-07, 0.0, 0.0, 5.1281042849045966e-05, 0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 1.521860949182208e-08, 0.0], [0.0, 0.0, 0.00016066151078753468, 0.0, 0.0, 6.203117823066924e-05, 0.0, 0.0, 3.707253325538521e-06, 0.0, 0.0, 4.767931105143542e-08, 0.0, 0.0, 0.0010471187546558576, 0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 2.4162193336805556e-05, 0.0, 0.0, 3.107520934310918e-07, 0.0, 0.0, 0.0005511334816329829, 0.0, 0.0, 0.00021279184454623816, 0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 1.635591783796321e-07, 0.0, 0.0, 5.1281042849045966e-05, 0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 1.521860949182208e-08], [6.203117823066924e-05, 0.0, 0.0, 2.3950148693507735e-05, 0.0, 0.0, 1.4313651767338148e-06, 0.0, 0.0, 1.840891341833803e-08, 0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 0.00015609619099706754, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 1.1998093630944017e-07, 0.0, 0.0, 0.0002127918445462381, 0.0, 0.0, 8.215862511424045e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 7.644572712981638e-06, 0.0, 0.0, 4.5687295358369104e-07, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0], [0.0, 6.203117823066924e-05, 0.0, 0.0, 2.3950148693507735e-05, 0.0, 0.0, 1.4313651767338148e-06, 0.0, 0.0, 1.840891341833803e-08, 0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 0.00015609619099706754, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 1.1998093630944017e-07, 0.0, 0.0, 0.0002127918445462381, 0.0, 0.0, 8.215862511424045e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 7.644572712981638e-06, 0.0, 0.0, 4.5687295358369104e-07, 0.0, 0.0, 5.875883235397876e-09, 0.0], [0.0, 0.0, 6.203117823066924e-05, 0.0, 0.0, 2.3950148693507735e-05, 0.0, 0.0, 1.4313651767338148e-06, 0.0, 0.0, 1.840891341833803e-08, 0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 0.00015609619099706754, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 1.1998093630944017e-07, 0.0, 0.0, 0.0002127918445462381, 0.0, 0.0, 8.215862511424045e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 7.644572712981638e-06, 0.0, 0.0, 4.5687295358369104e-07, 0.0, 0.0, 5.875883235397876e-09], [3.707253325538521e-06, 0.0, 0.0, 1.4313651767338148e-06, 0.0, 0.0, 8.55446158345398e-08, 0.0, 0.0, 1.1001968274067407e-09, 0.0, 0.0, 2.416219333680555e-05, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 5.575409515390106e-07, 0.0, 0.0, 7.170583210274754e-09, 0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 2.934523752997343e-07, 0.0, 0.0, 3.7741168061845776e-09, 0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 4.568729535836911e-07, 0.0, 0.0, 2.730471715728802e-08, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0], [0.0, 3.707253325538521e-06, 0.0, 0.0, 1.4313651767338148e-06, 0.0, 0.0, 8.55446158345398e-08, 0.0, 0.0, 1.1001968274067407e-09, 0.0, 0.0, 2.416219333680555e-05, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 5.575409515390106e-07, 0.0, 0.0, 7.170583210274754e-09, 0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 2.934523752997343e-07, 0.0, 0.0, 3.7741168061845776e-09, 0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 4.568729535836911e-07, 0.0, 0.0, 2.730471715728802e-08, 0.0, 0.0, 3.5116836865327755e-10, 0.0], [0.0, 0.0, 3.707253325538521e-06, 0.0, 0.0, 1.4313651767338148e-06, 0.0, 0.0, 8.55446158345398e-08, 0.0, 0.0, 1.1001968274067407e-09, 0.0, 0.0, 2.416219333680555e-05, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 5.575409515390106e-07, 0.0, 0.0, 7.170583210274754e-09, 0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 2.934523752997343e-07, 0.0, 0.0, 3.7741168061845776e-09, 0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 4.568729535836911e-07, 0.0, 0.0, 2.730471715728802e-08, 0.0, 0.0, 3.5116836865327755e-10], [4.767931105143542e-08, 0.0, 0.0, 1.840891341833803e-08, 0.0, 0.0, 1.1001968274067407e-09, 0.0, 0.0, 1.4149728153284066e-11, 0.0, 0.0, 3.107520934310917e-07, 0.0, 0.0, 1.1998093630944014e-07, 0.0, 0.0, 7.170583210274753e-09, 0.0, 0.0, 9.222150127904383e-11, 0.0, 0.0, 1.6355917837963207e-07, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 3.774116806184576e-09, 0.0, 0.0, 4.853924815628428e-11, 0.0, 0.0, 1.5218609491822077e-08, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0, 4.5164072724953534e-12, 0.0, 0.0], [0.0, 4.767931105143542e-08, 0.0, 0.0, 1.840891341833803e-08, 0.0, 0.0, 1.1001968274067407e-09, 0.0, 0.0, 1.4149728153284066e-11, 0.0, 0.0, 3.107520934310917e-07, 0.0, 0.0, 1.1998093630944014e-07, 0.0, 0.0, 7.170583210274753e-09, 0.0, 0.0, 9.222150127904383e-11, 0.0, 0.0, 1.6355917837963207e-07, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 3.774116806184576e-09, 0.0, 0.0, 4.853924815628428e-11, 0.0, 0.0, 1.5218609491822077e-08, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0, 4.5164072724953534e-12, 0.0], [0.0, 0.0, 4.767931105143542e-08, 0.0, 0.0, 1.840891341833803e-08, 0.0, 0.0, 1.1001968274067407e-09, 0.0, 0.0, 1.4149728153284066e-11, 0.0, 0.0, 3.107520934310917e-07, 0.0, 0.0, 1.1998093630944014e-07, 0.0, 0.0, 7.170583210274753e-09, 0.0, 0.0, 9.222150127904383e-11, 0.0, 0.0, 1.6355917837963207e-07, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 3.774116806184576e-09, 0.0, 0.0, 4.853924815628428e-11, 0.0, 0.0, 1.5218609491822077e-08, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0, 4.5164072724953534e-12], [0.0010471187546558576, 0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 2.416219333680555e-05, 0.0, 0.0, 3.107520934310917e-07, 0.0, 0.0, 0.006824644440210914, 0.0, 0.0, 0.002634985402269198, 0.0, 0.0, 0.00015747820167114296, 0.0, 0.0, 2.0253410009979323e-06, 0.0, 0.0, 0.003592037707773455, 0.0, 0.0, 0.0013868805924328934, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 0.00033422654537687156, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0], [0.0, 0.0010471187546558576, 0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 2.416219333680555e-05, 0.0, 0.0, 3.107520934310917e-07, 0.0, 0.0, 0.006824644440210914, 0.0, 0.0, 0.002634985402269198, 0.0, 0.0, 0.00015747820167114296, 0.0, 0.0, 2.0253410009979323e-06, 0.0, 0.0, 0.003592037707773455, 0.0, 0.0, 0.0013868805924328934, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 0.00033422654537687156, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 9.918798435640606e-08, 0.0], [0.0, 0.0, 0.0010471187546558576, 0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 2.416219333680555e-05, 0.0, 0.0, 3.107520934310917e-07, 0.0, 0.0, 0.006824644440210914, 0.0, 0.0, 0.002634985402269198, 0.0, 0.0, 0.00015747820167114296, 0.0, 0.0, 2.0253410009979323e-06, 0.0, 0.0, 0.003592037707773455, 0.0, 0.0, 0.0013868805924328934, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 0.00033422654537687156, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 9.918798435640606e-08], [0.0004042910450694799, 0.0, 0.0, 0.00015609619099706754, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 1.1998093630944014e-07, 0.0, 0.0, 0.002634985402269198, 0.0, 0.0, 0.0010173640738354993, 0.0, 0.0, 6.0802107159481916e-05, 0.0, 0.0, 7.819812473749775e-07, 0.0, 0.0, 0.0013868805924328932, 0.0, 0.0, 0.0005354726019452805, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 4.982385276881484e-05, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 3.8296338094876375e-08, 0.0, 0.0], [0.0, 0.0004042910450694799, 0.0, 0.0, 0.00015609619099706754, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 1.1998093630944014e-07, 0.0, 0.0, 0.002634985402269198, 0.0, 0.0, 0.0010173640738354993, 0.0, 0.0, 6.0802107159481916e-05, 0.0, 0.0, 7.819812473749775e-07, 0.0, 0.0, 0.0013868805924328932, 0.0, 0.0, 0.0005354726019452805, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 4.982385276881484e-05, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 3.8296338094876375e-08, 0.0], [0.0, 0.0, 0.0004042910450694799, 0.0, 0.0, 0.00015609619099706754, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 1.1998093630944014e-07, 0.0, 0.0, 0.002634985402269198, 0.0, 0.0, 0.0010173640738354993, 0.0, 0.0, 6.0802107159481916e-05, 0.0, 0.0, 7.819812473749775e-07, 0.0, 0.0, 0.0013868805924328932, 0.0, 0.0, 0.0005354726019452805, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 4.982385276881484e-05, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 3.8296338094876375e-08], [2.4162193336805556e-05, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 5.575409515390106e-07, 0.0, 0.0, 7.170583210274753e-09, 0.0, 0.0, 0.00015747820167114296, 0.0, 0.0, 6.0802107159481916e-05, 0.0, 0.0, 3.6337986863401713e-06, 0.0, 0.0, 4.673460447679087e-08, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 1.9125892957711578e-06, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 1.7795974459483417e-07, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0], [0.0, 2.4162193336805556e-05, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 5.575409515390106e-07, 0.0, 0.0, 7.170583210274753e-09, 0.0, 0.0, 0.00015747820167114296, 0.0, 0.0, 6.0802107159481916e-05, 0.0, 0.0, 3.6337986863401713e-06, 0.0, 0.0, 4.673460447679087e-08, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 1.9125892957711578e-06, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 1.7795974459483417e-07, 0.0, 0.0, 2.2887559257738496e-09, 0.0], [0.0, 0.0, 2.4162193336805556e-05, 0.0, 0.0, 9.328988094113968e-06, 0.0, 0.0, 5.575409515390106e-07, 0.0, 0.0, 7.170583210274753e-09, 0.0, 0.0, 0.00015747820167114296, 0.0, 0.0, 6.0802107159481916e-05, 0.0, 0.0, 3.6337986863401713e-06, 0.0, 0.0, 4.673460447679087e-08, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 1.9125892957711578e-06, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 1.7795974459483417e-07, 0.0, 0.0, 2.2887559257738496e-09], [3.107520934310918e-07, 0.0, 0.0, 1.1998093630944017e-07, 0.0, 0.0, 7.170583210274754e-09, 0.0, 0.0, 9.222150127904383e-11, 0.0, 0.0, 2.0253410009979323e-06, 0.0, 0.0, 7.819812473749775e-07, 0.0, 0.0, 4.673460447679087e-08, 0.0, 0.0, 6.01057858216645e-10, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 3.16356772895998e-10, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0, 3.829633809487638e-08, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0, 2.943589124434477e-11, 0.0, 0.0], [0.0, 3.107520934310918e-07, 0.0, 0.0, 1.1998093630944017e-07, 0.0, 0.0, 7.170583210274754e-09, 0.0, 0.0, 9.222150127904383e-11, 0.0, 0.0, 2.0253410009979323e-06, 0.0, 0.0, 7.819812473749775e-07, 0.0, 0.0, 4.673460447679087e-08, 0.0, 0.0, 6.01057858216645e-10, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 3.16356772895998e-10, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0, 3.829633809487638e-08, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0, 2.943589124434477e-11, 0.0], [0.0, 0.0, 3.107520934310918e-07, 0.0, 0.0, 1.1998093630944017e-07, 0.0, 0.0, 7.170583210274754e-09, 0.0, 0.0, 9.222150127904383e-11, 0.0, 0.0, 2.0253410009979323e-06, 0.0, 0.0, 7.819812473749775e-07, 0.0, 0.0, 4.673460447679087e-08, 0.0, 0.0, 6.01057858216645e-10, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 3.16356772895998e-10, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0, 3.829633809487638e-08, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0, 2.943589124434477e-11], [0.0005511334816329829, 0.0, 0.0, 0.0002127918445462381, 0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 1.6355917837963207e-07, 0.0, 0.0, 0.003592037707773455, 0.0, 0.0, 0.0013868805924328932, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 0.0018906091016322043, 0.0, 0.0, 0.0007299614548189094, 0.0, 0.0, 4.362567515369832e-05, 0.0, 0.0, 5.610736447798343e-07, 0.0, 0.0, 0.00017591456440703234, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 5.220594026364296e-08, 0.0, 0.0], [0.0, 0.0005511334816329829, 0.0, 0.0, 0.0002127918445462381, 0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 1.6355917837963207e-07, 0.0, 0.0, 0.003592037707773455, 0.0, 0.0, 0.0013868805924328932, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 0.0018906091016322043, 0.0, 0.0, 0.0007299614548189094, 0.0, 0.0, 4.362567515369832e-05, 0.0, 0.0, 5.610736447798343e-07, 0.0, 0.0, 0.00017591456440703234, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 5.220594026364296e-08, 0.0], [0.0, 0.0, 0.0005511334816329829, 0.0, 0.0, 0.0002127918445462381, 0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 1.6355917837963207e-07, 0.0, 0.0, 0.003592037707773455, 0.0, 0.0, 0.0013868805924328932, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 0.0018906091016322043, 0.0, 0.0, 0.0007299614548189094, 0.0, 0.0, 4.362567515369832e-05, 0.0, 0.0, 5.610736447798343e-07, 0.0, 0.0, 0.00017591456440703234, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 5.220594026364296e-08], [0.00021279184454623816, 0.0, 0.0, 8.215862511424045e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 0.0013868805924328934, 0.0, 0.0, 0.0005354726019452805, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 0.0007299614548189094, 0.0, 0.0, 0.00028183706777954424, 0.0, 0.0, 1.684381042869107e-05, 0.0, 0.0, 2.1662972723999476e-07, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 2.622395341765303e-05, 0.0, 0.0, 1.5672576483207097e-06, 0.0, 0.0, 2.0156638446381192e-08, 0.0, 0.0], [0.0, 0.00021279184454623816, 0.0, 0.0, 8.215862511424045e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 0.0013868805924328934, 0.0, 0.0, 0.0005354726019452805, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 0.0007299614548189094, 0.0, 0.0, 0.00028183706777954424, 0.0, 0.0, 1.684381042869107e-05, 0.0, 0.0, 2.1662972723999476e-07, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 2.622395341765303e-05, 0.0, 0.0, 1.5672576483207097e-06, 0.0, 0.0, 2.0156638446381192e-08, 0.0], [0.0, 0.0, 0.00021279184454623816, 0.0, 0.0, 8.215862511424045e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 0.0013868805924328934, 0.0, 0.0, 0.0005354726019452805, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 0.0007299614548189094, 0.0, 0.0, 0.00028183706777954424, 0.0, 0.0, 1.684381042869107e-05, 0.0, 0.0, 2.1662972723999476e-07, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 2.622395341765303e-05, 0.0, 0.0, 1.5672576483207097e-06, 0.0, 0.0, 2.0156638446381192e-08], [1.271736723116901e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 2.934523752997343e-07, 0.0, 0.0, 3.774116806184576e-09, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 1.9125892957711578e-06, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 4.362567515369832e-05, 0.0, 0.0, 1.684381042869107e-05, 0.0, 0.0, 1.0066594575118343e-06, 0.0, 0.0, 1.2946735812990036e-08, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 1.5672576483207099e-06, 0.0, 0.0, 9.366614167970075e-08, 0.0, 0.0, 1.2046484855430111e-09, 0.0, 0.0], [0.0, 1.271736723116901e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 2.934523752997343e-07, 0.0, 0.0, 3.774116806184576e-09, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 1.9125892957711578e-06, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 4.362567515369832e-05, 0.0, 0.0, 1.684381042869107e-05, 0.0, 0.0, 1.0066594575118343e-06, 0.0, 0.0, 1.2946735812990036e-08, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 1.5672576483207099e-06, 0.0, 0.0, 9.366614167970075e-08, 0.0, 0.0, 1.2046484855430111e-09, 0.0], [0.0, 0.0, 1.271736723116901e-05, 0.0, 0.0, 4.910157196173485e-06, 0.0, 0.0, 2.934523752997343e-07, 0.0, 0.0, 3.774116806184576e-09, 0.0, 0.0, 8.288602336880371e-05, 0.0, 0.0, 3.200217440517555e-05, 0.0, 0.0, 1.9125892957711578e-06, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 4.362567515369832e-05, 0.0, 0.0, 1.684381042869107e-05, 0.0, 0.0, 1.0066594575118343e-06, 0.0, 0.0, 1.2946735812990036e-08, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 1.5672576483207099e-06, 0.0, 0.0, 9.366614167970075e-08, 0.0, 0.0, 1.2046484855430111e-09], [1.635591783796321e-07, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 3.7741168061845776e-09, 0.0, 0.0, 4.853924815628428e-11, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 3.16356772895998e-10, 0.0, 0.0, 5.610736447798343e-07, 0.0, 0.0, 2.1662972723999476e-07, 0.0, 0.0, 1.2946735812990036e-08, 0.0, 0.0, 1.6650910788208463e-10, 0.0, 0.0, 5.220594026364297e-08, 0.0, 0.0, 2.0156638446381195e-08, 0.0, 0.0, 1.2046484855430113e-09, 0.0, 0.0, 1.5493090114499384e-11, 0.0, 0.0], [0.0, 1.635591783796321e-07, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 3.7741168061845776e-09, 0.0, 0.0, 4.853924815628428e-11, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 3.16356772895998e-10, 0.0, 0.0, 5.610736447798343e-07, 0.0, 0.0, 2.1662972723999476e-07, 0.0, 0.0, 1.2946735812990036e-08, 0.0, 0.0, 1.6650910788208463e-10, 0.0, 0.0, 5.220594026364297e-08, 0.0, 0.0, 2.0156638446381195e-08, 0.0, 0.0, 1.2046484855430113e-09, 0.0, 0.0, 1.5493090114499384e-11, 0.0], [0.0, 0.0, 1.635591783796321e-07, 0.0, 0.0, 6.314996352017353e-08, 0.0, 0.0, 3.7741168061845776e-09, 0.0, 0.0, 4.853924815628428e-11, 0.0, 0.0, 1.0660044358969375e-06, 0.0, 0.0, 4.115827794328041e-07, 0.0, 0.0, 2.459797913418078e-08, 0.0, 0.0, 3.16356772895998e-10, 0.0, 0.0, 5.610736447798343e-07, 0.0, 0.0, 2.1662972723999476e-07, 0.0, 0.0, 1.2946735812990036e-08, 0.0, 0.0, 1.6650910788208463e-10, 0.0, 0.0, 5.220594026364297e-08, 0.0, 0.0, 2.0156638446381195e-08, 0.0, 0.0, 1.2046484855430113e-09, 0.0, 0.0, 1.5493090114499384e-11], [5.1281042849045966e-05, 0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 1.5218609491822077e-08, 0.0, 0.0, 0.00033422654537687156, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0, 0.00017591456440703234, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 5.220594026364297e-08, 0.0, 0.0, 1.6368234948091398e-05, 0.0, 0.0, 6.319751970521768e-06, 0.0, 0.0, 3.7769589708859996e-07, 0.0, 0.0, 4.8575801486461375e-09, 0.0, 0.0], [0.0, 5.1281042849045966e-05, 0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 1.5218609491822077e-08, 0.0, 0.0, 0.00033422654537687156, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0, 0.00017591456440703234, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 5.220594026364297e-08, 0.0, 0.0, 1.6368234948091398e-05, 0.0, 0.0, 6.319751970521768e-06, 0.0, 0.0, 3.7769589708859996e-07, 0.0, 0.0, 4.8575801486461375e-09, 0.0], [0.0, 0.0, 5.1281042849045966e-05, 0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 1.5218609491822077e-08, 0.0, 0.0, 0.00033422654537687156, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0, 0.00017591456440703234, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 5.220594026364297e-08, 0.0, 0.0, 1.6368234948091398e-05, 0.0, 0.0, 6.319751970521768e-06, 0.0, 0.0, 3.7769589708859996e-07, 0.0, 0.0, 4.8575801486461375e-09], [1.9799536884913722e-05, 0.0, 0.0, 7.644572712981638e-06, 0.0, 0.0, 4.568729535836911e-07, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 4.982385276881484e-05, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 3.829633809487638e-08, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 2.622395341765303e-05, 0.0, 0.0, 1.5672576483207099e-06, 0.0, 0.0, 2.0156638446381195e-08, 0.0, 0.0, 6.319751970521768e-06, 0.0, 0.0, 2.440047145924604e-06, 0.0, 0.0, 1.4582784261427002e-07, 0.0, 0.0, 1.875504708585176e-09, 0.0, 0.0], [0.0, 1.9799536884913722e-05, 0.0, 0.0, 7.644572712981638e-06, 0.0, 0.0, 4.568729535836911e-07, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 4.982385276881484e-05, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 3.829633809487638e-08, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 2.622395341765303e-05, 0.0, 0.0, 1.5672576483207099e-06, 0.0, 0.0, 2.0156638446381195e-08, 0.0, 0.0, 6.319751970521768e-06, 0.0, 0.0, 2.440047145924604e-06, 0.0, 0.0, 1.4582784261427002e-07, 0.0, 0.0, 1.875504708585176e-09, 0.0], [0.0, 0.0, 1.9799536884913722e-05, 0.0, 0.0, 7.644572712981638e-06, 0.0, 0.0, 4.568729535836911e-07, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0, 0.0001290443884416787, 0.0, 0.0, 4.982385276881484e-05, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 3.829633809487638e-08, 0.0, 0.0, 6.792036029422062e-05, 0.0, 0.0, 2.622395341765303e-05, 0.0, 0.0, 1.5672576483207099e-06, 0.0, 0.0, 2.0156638446381195e-08, 0.0, 0.0, 6.319751970521768e-06, 0.0, 0.0, 2.440047145924604e-06, 0.0, 0.0, 1.4582784261427002e-07, 0.0, 0.0, 1.875504708585176e-09], [1.183306541232646e-06, 0.0, 0.0, 4.5687295358369104e-07, 0.0, 0.0, 2.730471715728802e-08, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 1.7795974459483417e-07, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 1.5672576483207097e-06, 0.0, 0.0, 9.366614167970075e-08, 0.0, 0.0, 1.2046484855430113e-09, 0.0, 0.0, 3.7769589708859996e-07, 0.0, 0.0, 1.4582784261427002e-07, 0.0, 0.0, 8.715306881283271e-09, 0.0, 0.0, 1.1208832826147877e-10, 0.0, 0.0], [0.0, 1.183306541232646e-06, 0.0, 0.0, 4.5687295358369104e-07, 0.0, 0.0, 2.730471715728802e-08, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 1.7795974459483417e-07, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 1.5672576483207097e-06, 0.0, 0.0, 9.366614167970075e-08, 0.0, 0.0, 1.2046484855430113e-09, 0.0, 0.0, 3.7769589708859996e-07, 0.0, 0.0, 1.4582784261427002e-07, 0.0, 0.0, 8.715306881283271e-09, 0.0, 0.0, 1.1208832826147877e-10, 0.0], [0.0, 0.0, 1.183306541232646e-06, 0.0, 0.0, 4.5687295358369104e-07, 0.0, 0.0, 2.730471715728802e-08, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0, 7.712254576456991e-06, 0.0, 0.0, 2.9776903991968186e-06, 0.0, 0.0, 1.7795974459483417e-07, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0, 4.059216490071937e-06, 0.0, 0.0, 1.5672576483207097e-06, 0.0, 0.0, 9.366614167970075e-08, 0.0, 0.0, 1.2046484855430113e-09, 0.0, 0.0, 3.7769589708859996e-07, 0.0, 0.0, 1.4582784261427002e-07, 0.0, 0.0, 8.715306881283271e-09, 0.0, 0.0, 1.1208832826147877e-10], [1.521860949182208e-08, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0, 4.5164072724953534e-12, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0, 3.8296338094876375e-08, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0, 2.943589124434477e-11, 0.0, 0.0, 5.220594026364296e-08, 0.0, 0.0, 2.0156638446381192e-08, 0.0, 0.0, 1.2046484855430111e-09, 0.0, 0.0, 1.5493090114499384e-11, 0.0, 0.0, 4.8575801486461375e-09, 0.0, 0.0, 1.875504708585176e-09, 0.0, 0.0, 1.1208832826147877e-10, 0.0, 0.0, 1.4415778472969945e-12, 0.0, 0.0], [0.0, 1.521860949182208e-08, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0, 4.5164072724953534e-12, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0, 3.8296338094876375e-08, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0, 2.943589124434477e-11, 0.0, 0.0, 5.220594026364296e-08, 0.0, 0.0, 2.0156638446381192e-08, 0.0, 0.0, 1.2046484855430111e-09, 0.0, 0.0, 1.5493090114499384e-11, 0.0, 0.0, 4.8575801486461375e-09, 0.0, 0.0, 1.875504708585176e-09, 0.0, 0.0, 1.1208832826147877e-10, 0.0, 0.0, 1.4415778472969945e-12, 0.0], [0.0, 0.0, 1.521860949182208e-08, 0.0, 0.0, 5.875883235397876e-09, 0.0, 0.0, 3.5116836865327755e-10, 0.0, 0.0, 4.5164072724953534e-12, 0.0, 0.0, 9.918798435640606e-08, 0.0, 0.0, 3.8296338094876375e-08, 0.0, 0.0, 2.2887559257738496e-09, 0.0, 0.0, 2.943589124434477e-11, 0.0, 0.0, 5.220594026364296e-08, 0.0, 0.0, 2.0156638446381192e-08, 0.0, 0.0, 1.2046484855430111e-09, 0.0, 0.0, 1.5493090114499384e-11, 0.0, 0.0, 4.8575801486461375e-09, 0.0, 0.0, 1.875504708585176e-09, 0.0, 0.0, 1.1208832826147877e-10, 0.0, 0.0, 1.4415778472969945e-12]]
}


@pytest.fixture
def element():
    nodes = []
    for ref_location, act_location in zip(DATA['ref_locations'], DATA['act_locations']):
        node = eq.Node()
        node.ref_location = ref_location
        node.act_location = act_location
        nodes.append(node)

    shape_functions = DATA['shape_functions']

    target = DATA['target']

    weight = DATA['weight']

    element = PointLocation(nodes)
    element.add(shape_functions, target, weight)

    return element


def test_element(element):
    f, g, h = element.compute_all()

    assert_almost_equal(f, DATA['exp_f'])
    assert_almost_equal(g, DATA['exp_g'])
    assert_almost_equal(h, DATA['exp_h'])
