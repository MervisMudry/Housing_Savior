# curl -X GET http://localhost:8888/Etudiant
# curl -X POST http://localhost:8888/Etudiant/\?Nom\=Cionaire\&Prenom\=Dick\&idAd\=2

import http.server, urllib.parse, sqlite3, os, threading, socketserver
import requests

class MyHandler(http.server.BaseHTTPRequestHandler):
	def __init__(self, *args, **kwargs):
		self.mysql = MySQL('logement.db')
		super(MyHandler, self).__init__(*args, **kwargs)

	def do_GET(self):
		# """Respond to a GET request."""
		#On récupère l'extension du fichier en vérifiant qu'il ne s'agitpas de l'adresse de base du site
		# print("\n\npath\n\n")
		# print(self.path)
		# print("\n\nsplit .\n\n")
		path_split = self.path.split('.')
		# print(path_split)
		# print("\n\nLen\n\n")
		length = len(path_split)
		# print(length)
		if (length >= 2):
			# print("\n\nExtension\n\n")
			extension = path_split[1]
			# print(extension)
		else:
			extension = "NULL"


		if(self.path == "/favicon.ico"):
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			return

		# Html


		elif (self.path == '/'):
			with open('website.html', 'r') as mon_fichier:

				fichier_html = mon_fichier.read()
				# print("\n\nOh\n\n")
				# print(fichier_html)
				# print("\n\nOh\n\n")
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))


		elif (self.path == '/table_adresse.html'):

			adresses_data = self.mysql.get_adressesdata()
			data = "<h4>Adresses</h4>\n"
			data += "		<table class=\"table table-bordered table-striped\">\n"
			data += "		<thead>\n"
			data += "		<tr>\n"
			data += "		<th>Id</th>\n"
			data += "		<th>Numero</th>\n"
			data += "		<th>Voie</th>\n"
			data += "		<th>Nom_voie</th>\n"
			data += "		<th>Code</th>\n"
			data += "		</tr>\n"
			data += "		</thead>\n"
			data += "		<tbody id=\"myTable\">\n"

			#On traite les adresses que l'on vient de récupérer

			# print(adresses_data)

			adresse_string = ""

			for i in range(len(adresses_data)):

				id = adresses_data[i][0]
				# print("\n\nid\n\n")
				# print(id)

				num = adresses_data[i][1]
				# print("\n\nNuméro\n\n")
				# print(num)

				voie = adresses_data[i][2]
				# print("\n\nvoie\n\n")
				# print(voie)

				nom_voie = adresses_data[i][3]
				# print("\n\nnom voie\n\n")
				# print(nom_voie)

				code = adresses_data[i][4]
				# print("\n\ncode\n\n")
				# print(code)

				data += "		<tr>\n"
				data += "		<td>" + str(id) + "</td>\n"
				data += "		<td>" + str(num) + "</td>\n"
				data += "		<td>" + voie + "</td>\n"
				data += "		<td>" + nom_voie + "</td>\n"
				data += "		<td>" + str(code) + "</td>\n"
				data += "		</tr>\n"


			data += "		</tbody>\n"
			data += "		 </table>\n"
			data += "		</div>\n"


			# print(data)



			with open('tables_start.html', 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()

				fichier_html += data

				with open('tables_end.html', 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print("\n\nOh\n\n")
					# print(fichier_html)
					# print("\n\nOh\n\n")
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif (self.path == '/table_ville.html'):

			villes_data = self.mysql.get_villesdata()
			data = "<h4>Villes</h4>\n"
			data += "		<table class=\"table table-bordered table-striped\">\n"
			data += "		<thead>\n"
			data += "		<tr>\n"
			data += "		<th>Ville</th>\n"
			data += "		<th>Code</th>\n"
			data += "		</tr>\n"
			data += "		</thead>\n"
			data += "		<tbody id=\"myTable\">\n"

			#On traite les villes que l'on vient de récupérer

			# print(villes_data)

			ville_string = ""

			for i in range(len(villes_data)):

				code = villes_data[i][0]
				# print("\n\nid\n\n")
				# print(id)

				ville = villes_data[i][1]
				# print("\n\nNuméro\n\n")
				# print(num)



				data += "		<tr>\n"
				data += "		<td>" + ville + "</td>\n"
				data += "		<td>" + str(code) + "</td>\n"
				data += "		</tr>\n"


			data += "		</tbody>\n"
			data += "		 </table>\n"
			data += "		</div>\n"


			# print(data)



			with open('tables_start.html', 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()

				fichier_html += data

				with open('tables_end.html', 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print("\n\nOh\n\n")
					# print(fichier_html)
					# print("\n\nOh\n\n")
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif (self.path == '/table_logement.html'):

			logements_data = self.mysql.get_logementsdata()
			data = "<h4>Logements</h4>\n"
			data += "		<table class=\"table table-bordered table-striped\">\n"
			data += "		<thead>\n"
			data += "		<tr>\n"
			data += "		<th>Id</th>\n"
			data += "		<th>Numero de telephone</th>\n"
			data += "		<th>Adresse IP</th>\n"
			data += "		<th>Date d'insertion</th>\n"
			data += "		<th>Id Adresse</th>\n"
			data += "		</tr>\n"
			data += "		</thead>\n"
			data += "		<tbody id=\"myTable\">\n"

			#On traite les logements que l'on vient de récupérer

			# print(logements_data)

			logement_string = ""

			for i in range(len(logements_data)):

				id = logements_data[i][0]
				# print("\n\nid\n\n")
				# print(id)

				num = logements_data[i][1]
				# print("\n\nNuméro\n\n")
				# print(num)

				ip = logements_data[i][2]
				# print("\n\nip\n\n")
				# print(ip)

				date = logements_data[i][3]
				# print("\n\nnom voie\n\n")
				# print(date)

				idAd = logements_data[i][4]
				# print("\n\nidAd\n\n")
				# print(idAd)

				data += "		<tr>\n"
				data += "		<td>" + str(id) + "</td>\n"
				data += "		<td>" + str(num) + "</td>\n"
				data += "		<td>" + ip + "</td>\n"
				data += "		<td>" + date + "</td>\n"
				data += "		<td>" + str(idAd) + "</td>\n"
				data += "		</tr>\n"


			data += "		</tbody>\n"
			data += "		 </table>\n"
			data += "		</div>\n"


			# print(data)



			with open('tables_start.html', 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()

				fichier_html += data

				with open('tables_end.html', 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print("\n\nOh\n\n")
					# print(fichier_html)
					# print("\n\nOh\n\n")
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif (self.path == '/table_piece.html'):

			pieces_data = self.mysql.get_piecesdata()
			data = "<h4>Pieces</h4>\n"
			data += "		<table class=\"table table-bordered table-striped\">\n"
			data += "		<thead>\n"
			data += "		<tr>\n"
			data += "		<th>Id</th>\n"
			data += "		<th>Coordonnee X</th>\n"
			data += "		<th>Coordonnee Y</th>\n"
			data += "		<th>Etage</th>\n"
			data += "		<th>Nom de la piece</th>\n"
			data += "		<th>Id Logement</th>\n"
			data += "		</tr>\n"
			data += "		</thead>\n"
			data += "		<tbody id=\"myTable\">\n"

			#On traite les pieces que l'on vient de récupérer

			# print(pieces_data)

			piece_string = ""

			for i in range(len(pieces_data)):

				id = pieces_data[i][0]
				# print("\n\nid\n\n")
				# print(id)

				coordX = pieces_data[i][1]
				# print("\n\nNuméro\n\n")
				# print(num)

				coordY = pieces_data[i][2]
				# print("\n\nNuméro\n\n")
				# print(num)

				etage = pieces_data[i][3]
				# print("\n\nNuméro\n\n")
				# print(num)

				nom = pieces_data[i][4]
				# print("\n\nnom voie\n\n")
				# print(nom_voie)

				idLog = pieces_data[i][5]
				# print("\n\ncode\n\n")
				# print(code)

				data += "		<tr>\n"
				data += "		<td>" + str(id) + "</td>\n"
				data += "		<td>" + str(coordX) + "</td>\n"
				data += "		<td>" + str(coordY) + "</td>\n"
				data += "		<td>" + str(etage) + "</td>\n"
				data += "		<td>" + nom + "</td>\n"
				data += "		<td>" + str(idLog) + "</td>\n"
				data += "		</tr>\n"


			data += "		</tbody>\n"
			data += "		 </table>\n"
			data += "		</div>\n"


			# print(data)



			with open('tables_start.html', 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()

				fichier_html += data

				with open('tables_end.html', 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print("\n\nOh\n\n")
					# print(fichier_html)
					# print("\n\nOh\n\n")
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif (self.path == '/table_type_capteur.html'):

			type_capteur_data = self.mysql.get_type_capteurdata()
			data = "<h4>Types de capteur</h4>\n"
			data += "		<table class=\"table table-bordered table-striped\">\n"
			data += "		<thead>\n"
			data += "		<tr>\n"
			data += "		<th>Id</th>\n"
			data += "		<th>Type</th>\n"
			data += "		<th>Unite</th>\n"
			data += "		<th>Plage</th>\n"
			data += "		</tr>\n"
			data += "		</thead>\n"
			data += "		<tbody id=\"myTable\">\n"

			#On traite les type_capteur que l'on vient de récupérer

			# print(type_capteur_data)

			adresse_string = ""

			for i in range(len(type_capteur_data)):

				id = type_capteur_data[i][0]
				# print("\n\nid\n\n")
				# print(id)

				type = type_capteur_data[i][1]
				# print("\n\nNuméro\n\n")
				# print(num)

				unite = type_capteur_data[i][2]
				# print("\n\nunite\n\n")
				# print(unite)

				plage = type_capteur_data[i][3]
				# print("\n\nnom unite\n\n")
				# print(plage)



				data += "		<tr>\n"
				data += "		<td>" + str(id) + "</td>\n"
				data += "		<td>" + type + "</td>\n"
				data += "		<td>" + unite + "</td>\n"
				data += "		<td>" + plage + "</td>\n"
				data += "		</tr>\n"


			data += "		</tbody>\n"
			data += "		 </table>\n"
			data += "		</div>\n"


			# print(data)



			with open('tables_start.html', 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()

				fichier_html += data

				with open('tables_end.html', 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print("\n\nOh\n\n")
					# print(fichier_html)
					# print("\n\nOh\n\n")
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif (self.path == '/table_capteur.html'):

			capteurs_data = self.mysql.get_capteursdata()
			data = "<h4>Capteurs</h4>\n"
			data += "		<table class=\"table table-bordered table-striped\">\n"
			data += "		<thead>\n"
			data += "		<tr>\n"
			data += "		<th>Id</th>\n"
			data += "		<th>Reference</th>\n"
			data += "		<th>Port</th>\n"
			data += "		<th>Date d'insertion</th>\n"
			data += "		<th>Id Type</th>\n"
			data += "		</tr>\n"
			data += "		</thead>\n"
			data += "		<tbody id=\"myTable\">\n"

			#On traite les capteurs que l'on vient de récupérer

			# print(capteurs_data)

			capteur_string = ""

			for i in range(len(capteurs_data)):

				id = capteurs_data[i][0]
				# print("\n\nid\n\n")
				# print(id)

				ref = capteurs_data[i][1]
				# print("\n\nNuméro\n\n")
				# print(ref)

				port = capteurs_data[i][2]
				# print("\n\nport\n\n")
				# print(port)

				date = capteurs_data[i][3]
				# print("\n\ndate\n\n")
				# print(date)

				id_Type = capteurs_data[i][4]
				# print("\n\nid_Type\n\n")
				# print(id_Type)

				data += "		<tr>\n"
				data += "		<td>" + str(id) + "</td>\n"
				data += "		<td>" + str(ref) + "</td>\n"
				data += "		<td>" + port + "</td>\n"
				data += "		<td>" + date + "</td>\n"
				data += "		<td>" + str(id_Type) + "</td>\n"
				data += "		</tr>\n"


			data += "		</tbody>\n"
			data += "		 </table>\n"
			data += "		</div>\n"


			# print(data)



			with open('tables_start.html', 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()

				fichier_html += data

				with open('tables_end.html', 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print("\n\nOh\n\n")
					# print(fichier_html)
					# print("\n\nOh\n\n")
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif (self.path == '/table_mesure.html'):

			mesures_data = self.mysql.get_mesuresdata()
			data = "<h4>Mesures</h4>\n"
			data += "		<table class=\"table table-bordered table-striped\">\n"
			data += "		<thead>\n"
			data += "		<tr>\n"
			data += "		<th>Id</th>\n"
			data += "		<th>Valeur</th>\n"
			data += "		<th>Date d'insertion</th>\n"
			data += "		<th>Id Capteur</th>\n"
			data += "		</tr>\n"
			data += "		</thead>\n"
			data += "		<tbody id=\"myTable\">\n"

			#On traite les mesures que l'on vient de récupérer

			# print(mesures_data)

			mesure_string = ""

			for i in range(len(mesures_data)):

				id = mesures_data[i][0]
				# print("\n\nid\n\n")
				# print(id)

				valeur = mesures_data[i][1]
				# print("\n\nNuméro\n\n")
				# print(valeur)

				date = mesures_data[i][2]
				# print("\n\ndate\n\n")
				# print(date)

				id_Cap = mesures_data[i][3]
				# print("\n\n\n\n")
				# print(id_Cap)

				data += "		<tr>\n"
				data += "		<td>" + str(id) + "</td>\n"
				data += "		<td>" + str(valeur) + "</td>\n"
				data += "		<td>" + date + "</td>\n"
				data += "		<td>" + str(id_Cap) + "</td>\n"
				data += "		</tr>\n"


			data += "		</tbody>\n"
			data += "		 </table>\n"
			data += "		</div>\n"


			# print(data)



			with open('tables_start.html', 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()

				fichier_html += data

				with open('tables_end.html', 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print("\n\nOh\n\n")
					# print(fichier_html)
					# print("\n\nOh\n\n")
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif (self.path == '/table_facture.html'):

			factures_data = self.mysql.get_facturesdata()
			data = "<h4>Factures</h4>\n"
			data += "		<table class=\"table table-bordered table-striped\">\n"
			data += "		<thead>\n"
			data += "		<tr>\n"
			data += "		<th>Id</th>\n"
			data += "		<th>Type</th>\n"
			data += "		<th>Date de la facture</th>\n"
			data += "		<th>Montant</th>\n"
			data += "		<th>Valeur</th>\n"
			data += "		<th>Id Logement</th>\n"
			data += "		</tr>\n"
			data += "		</thead>\n"
			data += "		<tbody id=\"myTable\">\n"

			#On traite les factures que l'on vient de récupérer

			# print(factures_data)

			facture_string = ""

			for i in range(len(factures_data)):

				id = factures_data[i][0]
				# print("\n\nid\n\n")
				# print(id)

				type = factures_data[i][1]
				# print("\n\nNuméro\n\n")
				# print(type)

				date = factures_data[i][2]
				# print("\n\ndate\n\n")
				# print(date)

				montant = factures_data[i][3]
				# print("\n\nmontant\n\n")
				# print(montant)

				valeur = factures_data[i][4]
				# print("\n\nvaleur\n\n")
				# print(valeur)

				id_Log = factures_data[i][5]
				# print("\n\nid_Log\n\n")
				# print(id_Log)

				data += "		<tr>\n"
				data += "		<td>" + str(id) + "</td>\n"
				data += "		<td>" + type + "</td>\n"
				data += "		<td>" + date + "</td>\n"
				data += "		<td>" + montant + "</td>\n"
				data += "		<td>" + str(valeur) + "</td>\n"
				data += "		<td>" + str(id_Log) + "</td>\n"

				data += "		</tr>\n"


			data += "		</tbody>\n"
			data += "		 </table>\n"
			data += "		</div>\n"


			# print(data)



			with open('tables_start.html', 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()

				fichier_html += data

				with open('tables_end.html', 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print("\n\nOh\n\n")
					# print(fichier_html)
					# print("\n\nOh\n\n")
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))


		elif (self.path == '/etat_capteur.html'):

			type_capteur_data = self.mysql.get_type_capteurdata()
			capteurs_data = self.mysql.get_capteursdata()
			mesures_data = self.mysql.get_mesuresdata()

			data = "<h4>Etat des capteurs</h4>\n"
			data += "		<table class=\"table table-bordered table-striped\">\n"
			data += "		<thead>\n"
			data += "		<tr>\n"
			data += "		<th>Id</th>\n"
			data += "		<th>Type de Capteur</th>\n"
			data += "		<th>Dernière valeur</th>\n"
			data += "		<th>Unite</th>\n"
			data += "		<th>Port</th>\n"
			data += "		<th>Reference</th>\n"
			data += "		<th>Etat</th>\n"
			data += "		</tr>\n"
			data += "		</thead>\n"
			data += "		<tbody id=\"myTable\">\n"

			#On traite les capteurs que l'on vient de récupérer
			# print("\n\nType capteur\n\n")
			# print(type_capteur_data)
			# print("\n\nCapteur\n\n")
			# print(capteurs_data)
			# print("\n\nMesure\n\n")
			# print(mesures_data)

			capteur_string = ""

			for i in range(len(capteurs_data)):



				id = capteurs_data[i][0]
				# print("\n\nid\n\n")
				# print(id)

				ref = capteurs_data[i][1]
				# print("\n\nRéférence\n\n")
				# print(ref)

				port = capteurs_data[i][2]
				# print("\n\nport\n\n")
				# print(port)

				id_Type = capteurs_data[i][4]
				# print("\n\nnom voie\n\n")
				# print(id_Type)

				id_Piece = capteurs_data[i][4]
				# print("\n\nid_Piece\n\n")
				# print(id_Piece)

				type_capteur = type_capteur_data[id_Type-1][1]
				unite = type_capteur_data[id_Type-1][2]

				#On cherche la dernière valeur
				for mesure in mesures_data:
					if (id == mesure[3]):
						last_mesure = mesure[1]

				data += "		<tr>\n"
				data += "		<td>" + str(id) + "</td>\n"
				data += "		<td>" + type_capteur + "</td>\n"
				data += "		<td>" + str(last_mesure) + "</td>\n"
				data += "		<td>" + unite + "</td>\n"
				data += "		<td>" + port + "</td>\n"

				data += "		<td>" + ref + "</td>\n"
				data += "		<td>" + "Rien a signaler" + "</td>\n"
				data += "		</tr>\n"


			data += "		</tbody>\n"
			data += "		 </table>\n"
			data += "		</div>\n"


			# print(data)



			with open('etat_capteur_start.html', 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()

				fichier_html += data

				with open('etat_capteur_end.html', 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print("\n\nOh\n\n")
					# print(fichier_html)
					# print("\n\nOh\n\n")
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))


		elif(self.path == '/eau_conso.html'):

			# print("\n\nEAU CONSOOO\n\n")
			# On récupère les données dans la base de données

			data = ""
			factures_data = self.mysql.get_facturesdata()


			#On traite les factures que l'on vient de récupérer

			# print(factures_data)

			for i in range(len(factures_data)):
				type = factures_data[i][1]
				# print("\n\ntype\n\n")
				# print(type)


				if (type == "Eau"):

					date = factures_data[i][2]
					# print("\n\ndate\n\n")
					# print(date)

					date = date.split('/')
					day = date[0]
					month = date[1]

					#Il faut ajuster l'indice du mois
					# print("\n\nMonth\n\n")
					# print(month)
					month = str(int(month) - 1)
					# print(month)
					year = date[2]
					# year = "2012"
					# print("\n\ndate split\n\n")
					# print(date)
					# print("\n\n")


					montant = factures_data[i][3].split('E')	#On récupère le montant sans l'indice pour que l'afichage fonctionne
					montant = montant[0]
					# print("\n\nmontant\n\n")
					# print(montant)

					valeur = factures_data[i][4].split('m')	#On récupère la valeur sans l'indice pour que l'afichage fonctionne
					valeur = valeur[0]


					data += "		var date = new Date(" + year + ", " + month + " ," + day +");\n"
					data += "		data.addRow([date, " + montant + ", " + valeur + "]);\n\n"

					# print(data)



			#On insère maintenant les datas entre deux fichiers htmls déjà rédigés
			with open("eau_conso_start.html", 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()


				fichier_html += data
				# print("\n\nOh\n\n")
				# print(fichier_html)
				# print("\n\nOh\n\n")

				with open("eau_conso_end.html", 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print(fichier_html)
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()

					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif(self.path == '/electricite_conso.html'):

			# On récupère les données dans la base de données

			data = ""
			factures_data = self.mysql.get_facturesdata()


			#On traite les factures que l'on vient de récupérer

			# print(factures_data)

			for i in range(len(factures_data)):
				type = factures_data[i][1]
				# print("\n\ntype\n\n")
				# print(type)


				if (type == "Electricite"):

					date = factures_data[i][2]
					# print("\n\ndate\n\n")
					# print(date)

					date = date.split('/')
					day = date[0]
					month = date[1]

					#Il faut ajuster l'indice du mois
					# print("\n\nMonth\n\n")
					# print(month)
					month = str(int(month) - 1)
					# print(month)

					year = date[2]
					# year = "2012"
					# print("\n\ndate split\n\n")
					# print(date)
					# print("\n\n")


					montant = factures_data[i][3].split('E')	#On récupère le montant sans l'indice pour que l'afichage fonctionne
					montant = montant[0]
					# print("\n\nmontant\n\n")
					# print(montant)

					valeur = factures_data[i][4].split('k')	#On récupère la valeur sans l'indice pour que l'afichage fonctionne
					valeur = valeur[0]


					data += "		var date = new Date(" + year + ", " + month + " ," + day +");\n"
					data += "		data.addRow([date, " + montant + ", " + valeur + "]);\n\n"

					# print(data)


			#On insère maintenant les datas entre deux fichiers htmls déjà rédigés
			with open("electricite_conso_start.html", 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()


				fichier_html += data
				# print("\n\nOh\n\n")
				# print(fichier_html)
				# print("\n\nOh\n\n")

				with open("electricite_conso_end.html", 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print(fichier_html)
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()

					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif(self.path == '/eau_eco.html'):

			# print("\n\nEAU CONSOOO\n\n")
			# On récupère les données dans la base de données

			data = ""
			factures_data = self.mysql.get_facturesdata()


			#On traite les factures que l'on vient de récupérer

			# print(factures_data)
			j = 0

			for i in range(len(factures_data)):
				type = factures_data[i][1]
				# print("\n\ntype\n\n")
				# print(type)


				if (type == "Eau"):

					date = factures_data[i][2]
					# print("\n\ndate\n\n")
					# print(date)

					date = date.split('/')
					day = date[0]
					month = date[1]

					#Il faut ajuster l'indice du mois
					# print("\n\nMonth\n\n")
					# print(month)
					month = str(int(month) - 1)
					# print(month)
					year = date[2]
					# year = "2012"
					# print("\n\ndate split\n\n")
					# print(date)
					# print("\n\n")


					montant = factures_data[i][3].split('E')	#On récupère le montant sans l'indice pour que l'afichage fonctionne
					montant = montant[0]
					# print("\n\nmontant\n\n")
					# print(montant)

					valeur = factures_data[i][4].split('m')	#On récupère la valeur sans l'indice pour que l'afichage fonctionne
					valeur = valeur[0]
					# print("\n\nj\n\n")
					# print(j)
					if (j == 0):
						# print("\n\nPremière montant\n\n")
						montant_prec = montant
						j = 7

					economie = str(float(montant_prec) - float(montant))

					data += "		var date = new Date(" + year + ", " + month + " ," + day +");\n"
					data += "		data.addRow([date, " + economie + "]);\n\n"

					#On enregistre la montant actuelle
					montant_prec = montant

			# print(data)



			#On insère maintenant les datas entre deux fichiers htmls déjà rédigés
			with open("eau_eco_start.html", 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()


				fichier_html += data
				# print("\n\nOh\n\n")
				# print(fichier_html)
				# print("\n\nOh\n\n")

				with open("eau_eco_end.html", 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print(fichier_html)
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()

					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		elif(self.path == '/electricite_eco.html'):

			# On récupère les données dans la base de données

			data = ""
			factures_data = self.mysql.get_facturesdata()


			#On traite les factures que l'on vient de récupérer

			# print(factures_data)
			j = 0
			for i in range(len(factures_data)):
				type = factures_data[i][1]
				# print("\n\ntype\n\n")
				# print(type)


				if (type == "Electricite"):

					date = factures_data[i][2]
					# print("\n\ndate\n\n")
					# print(date)



					date = date.split('/')
					day = date[0]
					month = date[1]

					#Il faut ajuster l'indice du mois
					# print("\n\nMonth\n\n")
					# print(month)
					month = str(int(month) - 1)
					# print(month)

					year = date[2]
					# year = "2012"
					# print("\n\ndate split\n\n")
					# print(date)
					# print("\n\n")


					montant = factures_data[i][3].split('E')	#On récupère le montant sans l'indice pour que l'afichage fonctionne
					montant = montant[0]
					# print("\n\nmontant\n\n")
					# print(montant)

					valeur = factures_data[i][4].split('k')	#On récupère la valeur sans l'indice pour que l'afichage fonctionne
					valeur = valeur[0]

					if (j == 0):
						# print("\n\nPremière montant\n\n")
						montant_prec = montant
						j = 7

					economie = str(float(montant_prec) - float(montant))


					data += "		var date = new Date(" + year + ", " + month + " ," + day +");\n"
					data += "		data.addRow([date, " + economie + "]);\n\n"

					#On enregistre la montant actuelle
					montant_prec = montant

			# print(data)


			#On insère maintenant les datas entre deux fichiers htmls déjà rédigés
			with open("electricite_eco_start.html", 'r') as mon_fichier_start:

				fichier_html = mon_fichier_start.read()


				fichier_html += data
				# print("\n\nOh\n\n")
				# print(fichier_html)
				# print("\n\nOh\n\n")

				with open("electricite_eco_end.html", 'r') as mon_fichier_end:

					fichier_html += mon_fichier_end.read()
					# print(fichier_html)
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()

					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))
		#On traite les requetes des autres pages html

		elif(extension == "html"):

			# print("\n\npath\n\n")
			# print(self.path)
			# print("\n\nlocal path\n\n")
			#On récupère l'extension du fichier en vérifiant qu'il ne s'agitpas de l'adresse de base du site
			# print("\n\npath\n\n")
			# print(self.path)
			# print("\n\nsplit /\n\n")
			path_split = self.path.split('/')
			# print(path_split)
			local_path = path_split[1]
			# print(local_path)

			with open(local_path, 'r') as mon_fichier:

				fichier_html = mon_fichier.read()
				# print("\n\nOh\n\n")
				# print(fichier_html)
				# print("\n\nOh\n\n")
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		#On traite les requetes des autres pages css
		elif(extension == "css"):

			# print("\n\npath\n\n")
			# print(self.path)
			# print("\n\nlocal path\n\n")
			# #On récupère l'extension du fichier en vérifiant qu'il ne s'agitpas de l'adresse de base du site
			# print("\n\npath\n\n")
			# print(self.path)
			# print("\n\nsplit /\n\n")
			path_split = self.path.split('/')
			local_path = path_split[1]
			# print(path_split)
			# print(local_path)

			with open(local_path, 'r') as mon_fichier:

				fichier_html = mon_fichier.read()
				# print("\n\nOh\n\n")
				# print(fichier_html)
				# print("\n\nOh\n\n")
				self.send_response(200)
				self.send_header("Content-type", "text/css")
				self.end_headers()

				self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))

		#On traite les requetes des autres pages javascript
		elif(extension == "js"):

			# print("\n\npath\n\n")
			# print(self.path)
			# print("\n\nlocal path\n\n")
			# #On récupère l'extension du fichier en vérifiant qu'il ne s'agitpas de l'adresse de base du site
			# print("\n\npath\n\n")
			# print(self.path)
			# print("\n\nsplit /\n\n")
			path_split = self.path.split('/')
			local_path = path_split[1]
			# print(path_split)
			# print(local_path)

			with open(local_path, 'r') as mon_fichier:

				fichier_html = mon_fichier.read()
				# print("\n\nOh\n\n")
				# print(fichier_html)
				# print("\n\nOh\n\n")
				self.send_response(200)
				self.send_header("Content-type", "text/js")
				self.end_headers()

				self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))
		#On traite les requetes d'images

		elif(extension == "jpg"):

			# print("\n\npath\n\n")
			# print(self.path)
			# print("\n\nlocal path\n\n")

			local_path = "images" + self.path
			# print(local_path)

			with open(local_path, 'rb') as mon_fichier:

					image = mon_fichier.read()
					self.send_response(200)
					self.send_header("Content-type", "image/jpg")
					self.send_header('Access-Control-Allow-Origin', '*')
					self.end_headers()
					self.wfile.write(bytes(image))

		elif(extension == "png"):

			# print("\n\npath\n\n")
			# print(self.path)
			# print("\n\nlocal path\n\n")

			local_path = "images" + self.path
			# print(local_path)

			with open(local_path, 'rb') as mon_fichier:

					image = mon_fichier.read()
					self.send_response(200)
					self.send_header("Content-type", "image/png")
					self.send_header('Access-Control-Allow-Origin', '*')
					self.end_headers()
					self.wfile.write(bytes(image))

		#On isole le cas de la météo car il n'y a pas de table correspondante

		elif(self.path == "/Meteo"):

			response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=43.61092&lon=3.87723&exclude=current,minutely,hourly&appid=d2753dda4d481c04a85af3a6cc95328d&units=metric")
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes(str(response.json())+'\n', 'UTF-8'))


		#On traite tous les autres cas
		else:

			res = urllib.parse.urlparse(self.path)
			rep = self.mysql.select(res.path)
			# print("ok\n")
			# print(str(res))
			# print("ok\n")
			# print(str(rep))
			# print("PATH\n")
			# print(self.path)
			if len(rep) > 0:
				#On isole le cas de la Facture car on veut afficher le PieChart
				if(self.path == "/Facture"):
					with open('fichier.html', 'w+') as mon_fichier:
						factures_string = ""
						factures_data = self.mysql.get_facturesdata()

						factures_string = factures_string + "<html>\n <head>\n  <script type =\"text/javascript\"	src = \"https://www.gstatic.com/charts/loader.js\"></script>\n  <script type = \"text/javascript\">\n		google.charts.load('current', {'packages': ['corechart']});\n		google.charts.setOnLoadCallback(drawChart);\n\n function drawChart() {\n\n		var data = google.visualization.arrayToDataTable([\n		['Type de Facture', 'Montant'],\n"

						#On ajoute les factures que l'on vient de récupérer

						for i in range(len(factures_data)):
							factures_string = factures_string + "		['"
							factures_string = factures_string + factures_data[i][1] + "_" + factures_data[i][2] + "'"
							valeur = factures_data[i][4].split('k')	#On récupère la valeur sans l'indice pour que l'afichage fonctionne
							# print(valeur[0])
							factures_string = factures_string + ", " + valeur[0] + "],\n"





						factures_string = factures_string + "		]);\n"
						factures_string = factures_string + "		var options = {\n			title: 'PieChart des Factures en fonction des valeurs'\n		};\n\n		var chart = new google.visualization.PieChart(document.getElementById('piechart'));\n		chart.draw(data, options);\n		}\n	</script>\n </head>\n <body>\n	<div id=\"piechart\" style=\"width: 900px; height: 500px;\"></div>\n </body>\n</html>"


						mon_fichier.write(factures_string)
						mon_fichier.close()
						self.send_response(200)
						self.send_header("Content-type", "text/html")
						self.end_headers()
						self.wfile.write(bytes(str(rep)+'\n', 'UTF-8'))
						self.wfile.write(bytes(str(factures_string)+'\n', 'UTF-8'))

				# elif(self.path == "/Capteur"):
				# 	print("Ok\n\n")
				else:
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					self.wfile.write(bytes(str(rep)+'\n', 'UTF-8'))

			else:
				self.send_response(404)
				self.send_header("Content-type", "text/html")
				self.end_headers()

	def do_POST(self):
		"""Respond to a POST request."""
		if (self.path == "/capteur_post.html"):

			q = self.rfile.read(int(self.headers['content-length'])).decode(encoding="utf-8") #On récupère la donnée du formulaire
			query = urllib.parse.parse_qs(q, keep_blank_values=1,encoding='utf-8') #On met les données au bon format
			path = "/Capteur"
			# print("\n\nq\n\n")
			# print(q)

			# print("\n\npath\n\n")
			# print(path)
			# print("\n\nquery\n\n")
			# print(query)
			# print("\n\nInfo reçu\n\n")
			print("\n\nOn post un capteur\n\n")
			rep = self.mysql.insert(path,query)


			if (rep == None):

				# print("\n\nq\n\n")
				# print(q)
				#
				# print("\n\npath\n\n")
				# print(path)
				# print("\n\nquery\n\n")
				# print(query)
				# print("\n\nInfo reçu\n\n")
				# print("\n\nOn post un capteur\n\n")
				Port = int(query['Port'][0])
				# print("ok\n")
				# print(Port)
				threading.Thread(target=serve_on_port, args=[Port]).start()
				print("Thread créé\n")

				#Affichage page de succès
				with open('succes.html', 'r') as mon_fichier:

					fichier_html = mon_fichier.read()
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()

					self.wfile.write(bytes(str(fichier_html)+'\n', 'UTF-8'))


			else :
				print("\n\nEchec lors de l'insertion dans la base de donnee\n\n")




		else:
			# print("\n\nDans le else\n\n")
			res = urllib.parse.urlparse(self.path)
			query = urllib.parse.parse_qs(res.query)
			rep = self.mysql.insert(res.path,query)


			# print("ok\n")
			# print(str(res))
			#
			# print("ok\n")
			# print(str(rep))
			#
			# print("ok\n")
			# print(self.path)
			Table = self.path.split('/')
			Table = Table[1]
			# print(Table)

			if(Table == "Capteur"):
				print("\n\nOn post un capteur\n\n")
				Port = int(query['Port'][0])
				# print("ok\n")
				# print(Port)
				threading.Thread(target=serve_on_port, args=[Port]).start()
				print("Thread créé\n")

			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()



class MySQL():
	def __init__(self, name):
		# print("Init\n")
		self.c = None
		self.req = None
		self.conn = sqlite3.connect(name)
		self.c = self.conn.cursor()

	def __exit__(self, exc_type, exc_value, traceback):
		self.conn.close()

	def select(self,path):
		elem = path.split('/')
		if len(elem) == 2:
			req = "select * from %s" %(elem[1])
		else:
			req = "select %s from %s where id=%s" %(elem[3],elem[1],elem[2])
		return self.c.execute(req).fetchall()

	def insert(self,path,query):
		print(query)
		attr = ', '.join(query.keys())
		val = ', '.join('"%s"' %v[0] for v in query.values())
		print(attr,val)
		req = "insert into %s (%s) values (%s)" %(path.split('/')[1], attr, val)
		print(req)
		self.c.execute(req)
		self.conn.commit()

	def get_villesdata(self):
		req = "SELECT * FROM Ville"
		ville_data = self.c.execute(req).fetchall()
		return ville_data

	def get_adressesdata(self):
		req = "SELECT * FROM Adresse"
		adresses_data = self.c.execute(req).fetchall()
		return adresses_data

	def get_logementsdata(self):
		req = "SELECT * FROM Logement"
		logements_data = self.c.execute(req).fetchall()
		return logements_data

	def get_piecesdata(self):
		req = "SELECT * FROM Piece"
		pieces_data = self.c.execute(req).fetchall()
		return pieces_data

	def get_type_capteurdata(self):
		req = "SELECT * FROM Type_Capteur"
		type_capteur_data = self.c.execute(req).fetchall()
		return type_capteur_data

	def get_capteursdata(self):
		req = "SELECT * FROM Capteur"
		capteurs_data = self.c.execute(req).fetchall()
		return capteurs_data

	def get_mesuresdata(self):
		req = "SELECT * FROM Mesure"
		mesures_data = self.c.execute(req).fetchall()
		return mesures_data

	def get_facturesdata(self):
		req = "SELECT * FROM Facture"
		factures_data = self.c.execute(req).fetchall()
		return factures_data


# if __name__ == '__main__':
# 	server_class = http.server.HTTPServer
# 	httpd = server_class(("localhost", 8888), MyHandler)
# 	try:
# 		httpd.serve_forever()

# 	except KeyboardInterrupt:
# 		pass
# 	httpd.server_close()

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
	pass

def serve_on_port(port):

	server = ThreadingHTTPServer(("localhost", port), MyHandler)

	# print("\n\n 2\n\n")

	Server_liste.append(server)
	# print(Server_liste)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print("\n\n C'est l'interrupt'\n\n")

	print("\n\n Fin serve_on_port\n\n")


def capteur_thread():
	print("Création d'un thread pour chaque capteur\n\n")
	conn = sqlite3.connect('logement.db')
	c = conn.cursor()
	c.execute('SELECT PORT FROM CAPTEUR')
	Port_liste = c.fetchall()
	print(Port_liste)

	for port in Port_liste:
			threading.Thread(target=serve_on_port, args=[int(port[0])]).start()
			print("\nThread crée \n\n")


	print("\nThreads créés \n\n")


if __name__ == '__main__':

	Server_liste = []

	capteur_thread()



	# httpd.server_close()
# 	# threading.Thread(target=serve_on_port, args=[7777]).start()
# 	# threading.Thread(target=serve_on_port, args=[8888]).start()
# 	# threading.Thread(target=serve_on_port, args=[9999]).start()
