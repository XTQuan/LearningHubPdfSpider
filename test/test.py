from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
drawing = svg2rlg("topic14.svg")
renderPDF.drawToFile(drawing, "test.pdf")