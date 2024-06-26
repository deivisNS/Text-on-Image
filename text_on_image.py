from PIL import Image, ImageEnhance, ImageDraw, ImageFont



class Text_on_Image():

	def __init__(self, img, text, font_size, save = None):
		
		self.image = Image.open(img)	#abrimos la imagen

		self.width, self.height = self.image.size  #obtenemos el ancho y largo de la imagen desempaquetandolo

		self.save_in = save

		self.text = text

		self.font_size = font_size

		self.font = ImageFont.truetype("ALGER.TTF", font_size)	#elegimos el tipo de letra y tamaño que se va a ingresar en la imagen


	def into_image(self, potition, text_color, up = 1.3):

		image = self.check_potition(potition, up) #verificamos si la posicion es aceptable

		if type(image) == str:

			return image

		draw = ImageDraw.Draw(image)	#instancia para comenzar a dibujar en la imagen

		draw.text((potition[0], potition[1]), self.text, font = self.font, fill = "red")	#agregamos el texto, 1. elegimos la posicion, 2. el texto, 3. la fuente definida anteriormente y 4. el color de letra

		if self.save_in == None:
	
			return image.show()	#si no se a especificado un lugar a guardar el resultado, entonces en vez de guardar el resultado, lo muestra

		else:

			image.save(f"{self.save_in}/into_imagen.jpg")	#guardamos la imagen si ya se ha especificado un lugar a guardar

			return "Se ha creado la Imagen."


	def sides_image(self, text_color, potition, up = 1.3):
		
		image = self.check_potition(potition, up) #verificamos si la posicion es aceptable

		if type(image) == str:

			return image

		if potition[1] == "top" or potition[1] == "bottom":

			new_height = (self.font_size * 2) + self.height
			
			new = Image.new("RGB", (self.width, new_height), "black")	#creamos una imagen en blanco, agregamos las dimensiones y un color de fondo

			if potition[1] == "top":

				new.paste(image, (0, self.font_size * 2))	#pegamos la imagen anterior a la que creamos en blanco y indicamos donde ira colocada

				new_height = self.font_size // 2

			elif potition[1] == "bottom":

				new.paste(image, (0, 0))	#pegamos la imagen anterior a la que creamos en blanco y indicamos donde ira colocada

				new_height = (self.font_size // 2) + self.height

			draw = ImageDraw.Draw(new)	#instancia para comenzar a dibujar en la imagen

			draw.text((potition[0], new_height), self.text, font = self.font, fill = text_color)	#agregamos el texto, 1. elegimos la posicion, 2. el texto, 3. la fuente definida anteriormente y 4. el color de letra

			if self.save_in == None:
	
				return new.show()	#si no se a especificado un lugar a guardar el resultado, entonces en vez de guardar el resultado, lo muestra

			else:

				new.save(f"{self.save_in}/side_imagen.jpg")	#guardamos la imagen si ya se ha especificado un lugar a guardar

				return "Se ha creado la Imagen."

		else:

			return "La Posicion es invalida."


	def check_potition(self, potition, up = 1.3):

		if type(potition[1]) == int:

			if potition[0] >= self.width or potition[1] >= self.height:

				return f"La Posicion se sale de la Imagen. El ancho de la Imagen es {self.width} y el alto de la Imagen es {self.height}."

		img_up = ImageEnhance.Contrast(self.image)	#instancia para mejorar la imagen

		image = img_up.enhance(up)	#aumentamos el contraste

		return image
		

add = Text_on_Image(
	"images/4.jpg",	#imagen a editar
	"HOLA MUNDO :).",	#texto que se agregara
	35,	#tamaño de letra
	save = "images/saves"	#donde se guardara, y si no se indica entonces el resultado solo se mostrara
	)

print(add.into_image(
	(100, 100),	#posicion donde se colocara el texto
	"red",	#color del texto
	up = 1.4  #si se quiere mejorar el contraste de la imagen, si no se indica entonces por defecto se mejorara un 1.3
	))

print(add.sides_image(
	"red",	#color del texto
	(100, "bottom"), #posicion donde se colocara el texto. 1. de izquierda a derecha en px y 2. bottom o top para abajo o arriba
	up = 1.1 #si se quiere mejorar el contraste de la imagen, si no se indica entonces por defecto se mejorara un 1.3
	))
