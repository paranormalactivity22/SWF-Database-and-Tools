import os, time, zlib, urllib, traceback, sys
from Tkinter import Tk; from tkFileDialog import askopenfilename, asksaveasfile

__developer__ = "Lucas"
__update__ = "29/08/2019"

print "[-] Created by : %s" %(__developer__)
print "[-] Updated at : %s" %(__update__)

def TFMUtil():
     try:
          Tk().withdraw()
          os.system('title TFMUtil [v2]')
          os.system('color 3')
          error = 0
          print("[-] TFMUtil\n")
          time.sleep(1.0)
          print("[-] Type 0: Decompress Swf")
          print("[-] Type 1: Compress Swf")
          print("[-] Type 2: Encript Swf")
          print("[-] Type 3: Download Langues")
          print("[-] Type 4: Decompress Langues")
          print("[-] Type 5: Compress Langues")
          print("[-] Type 6: Download Images")
          print("[-] Type 7: Info Download")
          print("[-] Type 8: Credits\n")
          util = int(input("[-] ->"))
          if (util == 0):
              print("[-] TFMUtil: Decompress Swf...")
              filename = askopenfilename()
              os.rename(filename, "tfm")
              os.system("abcexport tfm")
              os.system("rabcdasm tfm-0.abc")
              print("[-] TFMUtil: Finish\n")
          if (util == 1):
              print("[-] TFMUtil: Compress Swf...")
              name = askopenfilename()
              os.rename(name, ""+str(name)+".swf")
              os.system("rabcasm tfm-0/tfm-0.main.asasm")
              os.system("abcreplace tfm.swf 0 tfm-0/tfm-0.main.abc")
              os.remove("tfm-0.abc")
              print("[-] Finish\n")
          if (util == 2):
              print("[-] TFMUtil: Encript Swf...")
              openFile = askopenfilename()
              os.system("encript "+str(openFile)+" Transformice")
              os.remove(str(openFile))
              print("[-] Finish\n")
          if (util == 3):
              print("[-] TFMUtil: Create file...")
              try:
                  os.mkdir("langues")
              except Exception as Error:
                  print("[-] TFMUtil: "+str(Error))
              time.sleep(1.0)
              print("[-] TFMUtil: Download Langues...")
              langue = urllib.URLopener()
              for download in ["ar", "bg", "br", "cn", "cz", "de", "en", "es", "fi", "fr", "he", "hr", "hu", "id", "it", "jp", "lt", "lv", "nl", "ph", "pl", "ro", "ru", "sk", "tr", "vk"]:
                  langue.retrieve("https://universokeko.com/langues/tfz_"+str(download), "./langues/tfz_"+str(download))
                  print("https://www.miceforce.com/langues/tfz_"+str(download))
                  print("[-] Download langue: ["+str(download.upper())+"]")
              print("[-] Finish\n")
          if (util == 4):
              print("[-] TFMUtil: Decompress Langues...")
              try:
                  for use in ["ar", "bg", "br", "cn", "cz", "de", "en", "es", "fi", "fr", "he", "hr", "hu", "id", "it", "jp", "lt", "lv", "nl", "ph", "pl", "ro", "ru", "sk", "tr", "vk"]:
                      langue = open("./langues/tfz_"+str(use), 'rb').read()
                      decompress = zlib.decompress(langue)
                      file = open("./langues/tfz_"+str(use), 'wb')
                      file.write(decompress)
                      file.close()
                      print("[-] Langue Decompress: ["+str(use.upper())+"]")
              except Exception as Error:
                  print("[-] "+str(Error))
              print("[-] Finish\n")
          if (util == 5):
              print("[-] TFMUtil: Compress Langues...")
              try:
                  for use in ["ar", "bg", "br", "cn", "cz", "de", "en", "es", "fi", "fr", "he", "hr", "hu", "id", "it", "jp", "lt", "lv", "nl", "ph", "pl", "ro", "ru", "sk", "tr", "vk"]:
                      langue = open("./langues/tfz_"+str(use), 'rb').read()
                      compress = zlib.compress(langue)
                      file = open("./langues/tfz_"+str(use), 'wb')
                      file.write(compress)
                      file.close()
                      print("Langue Compress: ["+str(use.upper())+"]")
              except Exception as Error:
                  print("[-] "+str(Error))
              print("[-] Finish\n")
          if (util == 6):
              print("[-] TFMUtil: Create File...")
              try:
                  directory = ["images", "images/x_bibliotheques", "images/musiques", "images/x_transformice", "images/x_transformice/x_divers", "images/x_transformice/x_interface", "images/x_transformice/x_interface/x_icone_chamane", "images/x_transformice/x_interface/paiements", "images/x_transformice/x_interface/kongregate/", "images/x_transformice/x_connexion/", "images/x_transformice/x_badges", "images/x_transformice/x_inventaire", "images/x_transformice/x_mobile", "images/x_bouboum", "images/x_bouboum/x_interface", "images/x_commun", "images/x_commun/x_iconesjeux", "images/x_commun/x_image_stat", "images/x_commun/x_mode", "images/x_commun/x_iconespaiement", "images/divers", "images/x_divers", "images/x_forteresse", "images/x_forteresse/x_interfaces", "images/x_nekodancer", "images/x_nekodancer/x_interface", "images/x_nouveaute", "images/x_evenements", "images/x_transformice/x_evt", "images/x_transformice/x_evt/x_evt_03", "images/x_transformice/x_evt/x_evt_03/0or8meuj", "images/x_transformice/x_evt/x_evt_10", "images/x_transformice/x_evt/x_evt_10/YIKDFERT", "images/x_transformice/x_evt/x_evt_16", "images/x_transformice/x_evt/x_evt_16/JKESOLKA", "images/x_transformice/x_evt/x_evt_19", "images/x_transformice/x_evt/x_evt_19/svtrixcv", "images/x_transformice/x_aventure", "images/x_transformice/x_aventure/x_banniere"]
                  for files in directory:
                       os.mkdir(files, 0755)
              except Exception as Error:
                  print("[-] "+str(Error))
              download = urllib.URLopener()
              print("[-] TFMUtil: Download Musiques...")
              for music in ["tfm_0", "tfm_1", "tfm_2", "tfm_3"]:
                  download.retrieve("http://transformice.com/images/musiques/"+str(music)+".mp3", "./images/musiques/"+str(music)+".mp3")
                  print("[-] TFMUtil: Download Musiques: ["+str(music.upper())+"]")
              print("[-] TFMUtil: Download Binarys...")
              for binarys in ["x_fourrures", "x_fourrures2", "x_fourrures3", "x_meli_costumes", "x_pictos_editeur"]:
                  download.retrieve("http://transformice.com/images/x_bibliotheques/"+str(binarys)+".swf", "./images/x_bibliotheques/"+str(binarys)+".swf")
                  print("[-] TFMUtil: Download Binarys: ["+str(binarys.upper())+"]")
              print("[-] TFMUtil: Download Images...")
              for images in ["deesse.png", "defilante_mort.png", "defilante_plus.png", "defilante_saut.png", "defilante_vitesse.png", "defilante_coeur.png", "fond-niveau.png", "illu-niveau.png", "lvlup.png", "M_0.png", "M_1.png", "M_2.png", "M_3.png", "M_4.png", "x_achat_tenue.png", "x_flecheDroite.png", "x_flecheHaut.png", "x_iconeOptions.png", "x_illu_amis.jpg", "x_illu_tribu.jpg", "x_police.png", "x_bateaupirate.png", "x_evenements/x_machine_1.jpg", "x_evenements/x_machine_2.jpg", "x_evenements/x_machine_3.jpg", "divers/pika_surf.png", "x_nouveaute/x_halloween.jpg", "x_nouveaute/x_papaques_2015.jpg", "x_nouveaute/x_noel2016.jpg", "x_nouveaute/x_kredskongregate.jpg", "x_nouveaute/x_noel2015.jpg", "x_nouveaute/x_indi_flyer.jpg", "x_nekodancer/x_interface/x_cc.jpg", "x_nekodancer/x_deesse.png", "x_forteresse/x_interfaces/x_cc.jpg", "x_divers/x_steam.png", "x_commun/x_iconespaiement/x_logo_kongregate.png", "x_commun/x_iconespaiement/x_logo_g2apay.png", "x_commun/x_mode/x_18.jpg", "x_commun/x_mode/x_16.jpg", "x_commun/x_mode/x_11.jpg", "x_commun/x_mode/x_10.jpg", "x_commun/x_mode/x_9.jpg", "x_commun/x_mode/x_8.jpg", "x_commun/x_mode/x_3.jpg", "x_commun/x_mode/x_2.jpg", "x_commun/x_mode/x_1.jpg", "x_commun/x_image_stat/x_cadre.png", "x_commun/x_image_stat/x_33.jpg", "x_commun/x_image_stat/x_32.jpg", "x_commun/x_image_stat/x_31.jpg", "x_commun/x_image_stat/x_30.jpg", "x_commun/x_image_stat/x_29.jpg", "x_commun/x_image_stat/x_28.jpg", "x_commun/x_image_stat/x_27.jpg", "x_commun/x_image_stat/x_26.jpg", "x_commun/x_iconesjeux/x_tfm.jpg", "x_commun/x_iconesjeux/x_nk.jpg", "x_commun/x_iconesjeux/x_ft.jpg", "x_commun/x_iconesjeux/x_bb.jpg", "x_bouboum/x_interface/x_haut.jpg", "x_bouboum/x_interface/x_divers.png", "x_bouboum/x_interface/x_bas.jpg", "x_bouboum/x_interface/x_cc.jpg", "x_bouboum/x_chargement_serveur.png", "x_transformice/x_mobile/x_haut.png", "x_transformice/x_mobile/x_gauche.png", "x_transformice/x_mobile/x_droite.png", "x_transformice/x_mobile/x_bas.png", "x_transformice/x_evt/x_evt_03/0or8meuj/mongolfiere.png", "x_transformice/x_evt/x_evt_10/YIKDFERT/BOSS_AnvilGod.png", "x_transformice/x_evt/x_evt_16/JKESOLKA/tardis.png", "x_transformice/x_evt/x_evt_19/svtrixcv/bateau.png", "x_transformice/x_connexion/x_indi.jpg", "x_transformice/x_connexion/x_noel2014.jpg", "x_transformice/x_connexion/x_papaque_2015.jpg", "x_transformice/x_connexion/x_rentray.jpg", "x_transformice/x_connexion/x_chamanes.jpg"]:
                  download.retrieve("http://transformice.com/images/"+str(images), "./images/"+str(images))
                  print("[-] TFMUtil: Download Images: ["+str(images.upper())+"]")
              for images in ["x_transformice/x_aventure/x_banniere/x_1.jpg", "x_transformice/x_aventure/x_banniere/x_2.jpg", "x_transformice/x_aventure/x_banniere/x_3.jpg", "x_transformice/x_aventure/x_banniere/x_4.jpg", "x_transformice/x_aventure/x_banniere/x_5.jpg", "x_transformice/x_aventure/x_banniere/x_6.jpg", "x_transformice/x_aventure/x_banniere/x_7.jpg", "x_transformice/x_aventure/x_banniere/x_8.jpg", "x_transformice/x_aventure/x_banniere/x_9.jpg", "x_transformice/x_aventure/x_banniere/x_10.jpg", "x_transformice/x_aventure/x_banniere/x_11.jpg", "x_transformice/x_aventure/x_banniere/x_12.jpg", "x_transformice/x_aventure/x_banniere/x_13.jpg", "x_transformice/x_aventure/x_banniere/x_14.jpg", "x_transformice/x_aventure/x_banniere/x_15.jpg", "x_transformice/x_aventure/x_banniere/x_16.jpg", "x_transformice/x_aventure/x_banniere/x_17.jpg", "x_transformice/x_aventure/x_banniere/x_18.jpg", "x_transformice/x_aventure/x_banniere/x_19.jpg", "x_transformice/x_aventure/x_banniere/x_20.jpg", "x_transformice/x_aventure/x_banniere/x_21.jpg", "x_transformice/x_aventure/x_banniere/x_22.jpg", "x_transformice/x_aventure/x_banniere/x_23.jpg", "x_transformice/x_aventure/x_banniere/x_52.jpg", "x_transformice/x_divers/x_cadeau1.jpg", "x_transformice/x_divers/x_cadeau2.jpg", "x_transformice/x_divers/x_fond_message.jpg", "x_transformice/x_divers/x_taxe.png", "x_transformice/x_divers/x_tribunal.png", "x_transformice/x_divers/x_xp_chamane.png", "x_transformice/x_interface/1.jpg", "x_transformice/x_interface/2.png", "x_transformice/x_interface/3.png", "x_transformice/x_interface/4.jpg", "x_transformice/x_interface/x_election.png", "x_transformice/x_interface/x_envoyer.png", "x_transformice/x_interface/x_fermer.png", "x_transformice/x_interface/x_fond_dessin_halloween.jpg", "x_transformice/x_interface/x_fond_dessin_noel.jpg", "x_transformice/x_interface/x_lettre.png", "x_transformice/x_interface/x_reset.png", "x_transformice/x_interface/croix.png", "x_transformice/x_interface/pinceau.png", "x_transformice/x_interface/paiements/hipay.jpg", "x_transformice/x_interface/paiements/paypal.jpg", "x_transformice/x_interface/kongregate/fond-invite.png", "x_transformice/x_interface/kongregate/fond-tfm.png", "x_transformice/x_interface/kongregate/fond.jpg", "x_transformice/x_interface/kongregate/kong.png"]:
                  download.retrieve("http://transformice.com/images/"+str(images), "./images/"+str(images))
                  print("[-] TFMUtil: Download Images: ["+str(images.upper())+"]")
              print("[-] TFMUtil: Download Chaman Icones...")
              for images in ["x_i_1.png", "x_i_2.png", "x_i_3.png", "x_i_4.png", "x_i_5.png", "x_i_6.png", "x_i_7.png", "x_i_8.png", "x_i_9.png", "x_i_10.png", "x_i_11.png", "x_i_12.png", "x_i_13.png", "x_i_14.png", "x_i_15.png", "x_i_16.png", "x_i_17.png", "x_i_18.png", "x_i_19.png", "x_i_20.png", "x_i_21.png", "x_i_22.png", "x_i_23.png", "x_i_24.png", "x_i_25.png", "x_i_26.png", "x_i_27.png", "x_i_28.png", "x_i_29.png", "x_i_30.png", "x_i_31.png", "x_i_32.png", "x_i_33.png", "x_i_34.png", "x_i_35.png", "x_i_36.png", "x_i_37.png", "x_i_38.png", "x_i_39.png", "x_i_40.png", "x_i_41.png", "x_i_42.png", "x_i_43.png", "x_i_44.png", "x_i_45.png", "x_i_46.png", "x_i_60.png", "x_i_61.png", "x_i_62.png", "x_i_63.png", "x_i_64.png", "x_i_65.png", "x_i_66.png", "x_i_67.png", "x_i_68.png", "x_i_69.png", "x_i_70.png", "x_i_71.png", "x_i_72.png", "x_i_73.png", "x_i_74.png", "x_i_80.png", "x_i_81.png", "x_i_82.png", "x_i_83.png", "x_i_84.png", "x_i_85.png", "x_i_86.png", "x_i_87.png", "x_i_88.png", "x_i_89.png", "x_i_90.png", "x_i_91.png", "x_i_92.png", "x_i_93.png", "x_i_94.png"]:
                  download.retrieve("http://transformice.com/images/x_transformice/x_interface/x_icone_chamane/"+str(images), "./images/x_transformice/x_interface/x_icone_chamane/"+str(images))
                  print("[-] TFMUtil: Download Chaman Icones: ["+str(images.upper())+"]")
              print("[-] TFMUtil: Download Inventaire...")
              for images in ["tag_oeuf.jpg", "1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg", "11.jpg", "12.jpg", "13.jpg", "14.jpg", "15.jpg", "16.jpg", "17.jpg", "18.jpg", "19.jpg", "20.jpg", "21.jpg", "22.jpg", "23.jpg", "24.jpg", "25.jpg", "26.jpg", "27.jpg", "28.jpg", "29.jpg", "30.jpg", "31.jpg", "32.jpg", "33.jpg", "34.jpg", "35.jpg", "2000.jpg", "2100.jpg", "2101.jpg", "2102.jpg", "2103.jpg", "2104.jpg", "2111.jpg", "2112.jpg", "2113.jpg", "2114.jpg", "2115.jpg", "2116.jpg", "2118.jpg", "2119.jpg", "2120.jpg", "2121.jpg", "2122.jpg", "2123.jpg", "2125.jpg", "2126.jpg", "2127.jpg", "2128.jpg", "2129.jpg", "2130.jpg", "2132.jpg", "2133.jpg", "2134.jpg", "2135.jpg", "2136.jpg", "2137.jpg", "2139.jpg", "2140.jpg", "2141.jpg", "2142.jpg", "2143.jpg", "2144.jpg", "2146.jpg", "2147.jpg", "2.jpg", "2149.jpg", "2150.jpg", "2151.jpg", "2153.jpg", "2154.jpg", "2155.jpg", "2156.jpg", "2157.jpg", "2158.jpg", "2160.jpg", "2161.jpg", "2162.jpg", "2163.jpg", "2164.jpg", "2165.jpg", "2167.jpg", "2168.jpg", "2169.jpg", "2170.jpg", "2171.jpg", "2172.jpg", "2174.jpg", "2175.jpg", "2176.jpg", "2177.jpg", "2178.jpg", "2179.jpg", "2190.jpg", "2191.jpg", "2192.jpg", "2193.jpg", "2194.jpg", "2195.jpg", "2196.jpg", "2197.jpg", "2198.jpg", "2199.jpg", "2200.jpg", "2201.jpg", "2202.jpg", "2203.jpg", "2204.jpg", "2210.jpg", "2211.jpg", "2212.jpg", "2213.jpg", "2214.jpg", "2215.jpg", "2216.jpg", "2217.jpg", "2218.jpg", "2219.jpg", "2220.jpg", "2221.jpg", "2222.jpg", "2223.jpg", "2224.jpg", "2225.jpg", "2226.jpg", "2227.jpg", "2232.jpg", "2233.jpg", "2234.jpg", "2235.jpg", "2236.jpg", "2237.jpg", "2238.jpg", "2239.jpg", "2240.jpg", "2241.jpg", "2242.jpg", "2243.jpg", "2244.jpg", "2245.jpg", "2246.jpg", "2247.jpg", "2248.jpg", "2249.jpg", "2250.jpg", "2251.jpg", "2252.jpg", "2253.jpg", "2254.jpg", "2255.jpg", "2256.jpg", "2257.jpg", "2258.jpg", "2259.jpg", "2260.jpg", "2261.jpg", "2262.jpg", "2263.jpg", "2264.jpg", "2265.jpg", "2266.jpg", "2267.jpg", "2268.jpg", "2269.jpg", "2270.jpg", "2271.jpg", "2272.jpg", "2273.jpg", "2274.jpg", "2275.jpg", "2276.jpg", "2277.jpg", "2278.jpg", "2279.jpg", "2280.jpg", "2281.jpg", "2282.jpg", "2283.jpg", "2284.jpg", "2285.jpg", "2286.jpg", "2287.jpg", "2288.jpg", "2289.jpg", "2290.jpg", "2291.jpg", "2292.jpg", "2293.jpg", "2294.jpg", "2295.jpg", "2296.jpg", "2297.jpg", "2298.jpg", "2299.jpg", "2300.jpg", "2301.jpg", "2302.jpg", "2303.jpg", "2304.jpg", "2305.jpg", "2306.jpg", "2308.jpg", "2310.jpg", "2311.jpg", "2312.jpg", "2313.jpg", "2314.jpg", "2315.jpg", "2316.jpg", "2317.jpg", "2318.jpg", "2319.jpg", "2320.jpg", "2321.jpg", "2323.jpg", "2324.jpg", "2325.jpg", "2326.jpg", "2327.jpg", "2328.jpg", "2330.jpg", "2332.jpg", "2334.jpg", "2335.jpg", "2336.jpg", "2337.jpg", "2338.jpg", "2339.jpg", "2340.jpg"]:
                  download.retrieve("http://transformice.com/images/x_transformice/x_inventaire/"+str(images), "./images/x_transformice/x_inventaire/"+str(images))
                  print("[-] TFMUtil: Download Inventaire: ["+str(images.upper())+"]")
              print("[-] TFMUtil: Download Badges...")
              for images in ["x_0.png", "x_1.png", "x_2.png", "x_3.png", "x_4.png", "x_5.png", "x_6.png", "x_7.png", "x_8.png", "x_9.png", "x_10.png", "x_11.png", "x_12.png", "x_13.png", "x_14.png", "x_15.png", "x_16.png", "x_17.png", "x_18.png", "x_19.png", "x_20.png", "x_21.png", "x_22.png", "x_23.png", "x_24.png", "x_25.png", "x_26.png", "x_27.png", "x_28.png", "x_29.png", "x_30.png", "x_31.png", "x_32.png", "x_33.png", "x_34.png", "x_35.png", "x_36.png", "x_37.png", "x_38.png", "x_39.png", "x_40.png", "x_41.png", "x_42.png", "x_43.png", "x_44.png", "x_45.png", "x_46.png", "x_47.png", "x_48.png", "x_49.png", "x_50.png", "x_51.png", "x_52.png", "x_53.png", "x_54.png", "x_55.png", "x_56.png", "x_57.png", "x_58.png", "x_59.png", "x_60.png", "x_61.png", "x_62.png", "x_63.png", "x_64.png", "x_65.png", "x_66.png", "x_67.png", "x_68.png", "x_69.png", "x_70.png", "x_71.png", "x_72.png", "x_73.png", "x_120.png", "x_121.png", "x_122.png", "x_123.png", "x_124.png", "x_125.png", "x_126.png", "x_127.png", "x_128.png", "x_129.png", "x_130.png", "x_131.png", "x_132.png", "x_133.png", "x_134.png", "x_135.png", "x_136.png", "x_137.png", "x_138.png", "x_139.png", "x_140.png", "x_141.png", "x_142.png", "x_143.png", "x_144.png", "x_145.png", "x_146.png", "x_147.png", "x_148.png", "x_149.png", "x_150.png", "x_151.png", "x_152.png", "x_153.png", "x_154.png", "x_155.png", "x_156.png", "x_157.png", "x_158.png", "x_160.png", "x_161.png", "x_162.png", "x_163.png", "x_165.png", "x_167.png", "x_169.png", "x_170.png", "x_171.png", "x_173.png", "x_174.png", "x_175.png", "x_176.png", "x_177.png", "x_178.png", "x_179.png", "x_180.png", "x_181.png", "x_182.png", "x_183.png", "x_184.png", "x_185.png", "x_186.png", "x_187.png", "x_188.png", "x_189.png", "x_190.png", "x_191.png", "x_192.png", "x_193.png", "x_194.png", "x_195.png", "x_196.png", "x_197.png", "x_198.png", "x_199.png", "x_200.png", "x_201.png", "x_202.png", "x_203.png", "x_204.png", "x_205.png", "x_206.png", "x_207.png", "x_208.png", "x_209.png", "x_210.png", "x_211.png", "x_212.png", "x_213.png", "x_214.png", "x_215.png", "x_216.png", "x_217.png", "x_218.png", "x_219.png", "x_220.png", "x_221.png", "x_222.png", "x_223.png", "x_224.png", "x_225.png", "x_226.png", "x_227.png", "x_228.png", "x_229.png", "x_230.png", "x_231.png", "x_232.png", "x_233.png", "x_234.png", "x_235.png", "x_236.png", "x_237.png", "x_238.png", "x_239.png", "x_240.png", "x_241.png", "x_242.png", "x_243.png", "x_244.png", "x_245.png", "x_246.png", "x_247.png", "x_248.png", "x_249.png", "x_250.png", "x_251.png"]:
                  download.retrieve("http://transformice.com/images/x_transformice/x_badges/"+str(images), "./images/x_transformice/x_badges/"+str(images))
                  print("[-] TFMUtil: Download Badges: ["+str(images.upper())+"]")
              print("[-] Finish\n")
          if (util == 7):
              print("[-] TFMUtil: Info download...")
              time.sleep(1.0)
              print("[EN]: I want to give a warning that the downloads of (images, langues) are very reliable, since our download addresses come from the server original: www.transformice.com. Errors in the system, lack of information or something sercan, please contact the author.\n")
              print("[ES]: Quiero dar una advertencia de que las descargas de (imagenes, langues) son muy confiables, ya que nuestras direcciones de descarga provienen del servidor original: www.transformice.com. Errores en el sistema, falta de informacion o algo sercano, porfavor contactese con el autor.\n")
          if (util == 8):
              print("[-] TFMUtil: Credits...")
              print("[-] %s: Developer") %(__developer__)
              print("[-] Kira (Encript.exe)")
              print("[-] TFMUtil, use: rabcasm")
          if not (util in [0,1,2,3,4,5,6,7,8]):
              print("[-] System have 10 types\n")
          TFMReset()
     except Exception as Error:
         print("[-] "+str(Error))
         TFMReset()

def TFMReset():
    print("[-] Type 1: Reset TFMUtil")
    print("[-] Type 2: Close TFMUtil")
    reset = int(input("->"))
    if (reset == 1):
        TFMUtil()
    if (reset == 2):
        print("[-] Thanks...")
        time.sleep(1.0)
        sys.exit()
		 
if __name__ == "__main__":
    TFMUtil()
    input()
