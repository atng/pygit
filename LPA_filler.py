import os
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import blue, black, white
import pdfrw
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject, TextStringObject

ANNOTATIONS_KEY = "/Annots"


class LPAFormFill:

    c = canvas.Canvas("output.pdf")
    form = c.acroForm
    generated_pages = []

    def set_check_box(self, checked=False, coordinates=[]):
        """Sets a checkbox
        """

        # name the parameter's name None
        # x the horizontal position on the page (absolute coordinates) 0
        # y the vertical position on the page (absolute coordinates) 0
        # size The outline dimensions size x size 20
        # checked if True the checkbox is initially checked False
        # buttonStyle the checkbox style (see below) 'check'
        # shape The outline of the widget (see below) 'square'
        # fillColor colour to be used to fill the widget None
        # textColor the colour of the symbol or text None
        # borderWidth as it says 1
        # borderColor the widget's border colour None
        # borderStyle The border style name 'solid'
        # tooltip The text to display when hovering over the widget None
        # annotationFlags blank separated string of annotation flags 'print'
        # fieldFlags Blank separated field flags (see below) 'required'
        # forceBorder when true a border force a border to be drawn False
        # relative if true obey the current canvas transform False
        # dashLen the dashline to be used if the borderStyle=='dashed' 3

        if coordinates:
            x1 = float(coordinates[0])
            y1 = float(coordinates[1])
            x2 = float(coordinates[2])
            y2 = float(coordinates[3])
        else:
            x1 = x2 = y1 = y2 = 0

        size = x2 - x1

        self.form.checkbox(
            name="cb1",
            x=x1,
            y=y1,
            size=size,
            checked=checked,
            buttonStyle="check",
            borderWidth=0,
            forceBorder=True)

        return self

    def set_text_box(self, value='', coordinates=[]):
        """Sets a textbox
        """

        # name the radio's group (ie parameter) name None
        # value Value of the text field ''
        # maxlen None or maximum length of the widget value 100
        # x the horizontal position on the page (absolute coordinates) 0
        # y the vertical position on the page (absolute coordinates) 0
        # width The widget width 120
        # height The widget height 36
        # fontName The name of the type 1 font to be used 'Helvetica'
        # Parameter Meaning Default
        # fontSize The size of font to be used 12
        # fillColor colour to be used to fill the widget None
        # textColor the colour of the symbol or text None
        # borderWidth as it says 1
        # borderColor the widget's border colour None
        # borderStyle The border style name 'solid'
        # tooltip The text to display when hovering over the widget None
        # annotationFlags blank separated string of annotation flags 'print'
        # fieldFlags Blank separated field flags (see below) ''
        # forceBorder when true a border force a border to be drawn False
        # relative if true obey the current canvas transform False
        # dashLen the dashline to be used if the borderStyle=='dashed' 3
        if coordinates:
            x1 = float(coordinates[0])
            y1 = float(coordinates[1])
            x2 = float(coordinates[2])
            y2 = float(coordinates[3])
        else:
            x1 = x2 = y1 = y2 = 0

        width = x2 - x1
        height = y2 - y1

        self.form.textfield(
            name="fname",
            value=value,
            borderWidth=0,
            x=x1,
            y=y1,
            width=width,
            fontSize=9.5,
            height=height,
            textColor=black,
        )

        return self

    def get_template(self):
        template = pdfrw.PdfReader('LPA_form.pdf')
        return template

    def get_pages(self, template=None):
        if not template:
            template = self.get_template()
        return template.Root.Pages.Kids

    def fields_on_page_exists(self, page):
        return True if page.Annots else False

    def get_fields_on_page(self, page=None):
        if self.fields_on_page_exists(page):
            return page.Annots
        else:
            return None

    def generate_page(self, page):
        fields = self.get_fields_on_page(page)
        if fields:
            for field in fields:
                if '/AS' in field:
                    self.set_check_box(
                        checked=True, coordinates=field["/Rect"])
                else:
                    self.set_text_box(
                        value="HELLO", coordinates=field["/Rect"])

    # def get_trial():
    #     outfile = "myOutputPdf.pdf"
    #     outputStream = open(outfile, "wb")
    #     template = pdfrw.PdfReader('LPA_form.pdf')
    #     field_dictionary = {"(Country of issue 1)": "(Hello)"}
    #     for pages in template.Root.Pages.Kids:
    #         print(pages.Annots)
    #         if pages.Annots:
    #             for field in pages.Annots:
    #                 if field['/Border'] == ['0', '0', '1']:
    #                     print(field)
    #     for fields in template.Root.AcroForm.Fields:
    #         import pprint
    #         pp = pprint.PrettyPrinter(indent=4)
    #         pp.pprint(field)
    #         if field['/FT'] == '/Btn':
    #             import pprint
    #             pp = pprint.PrettyPrinter(indent=4)
    #             pp.pprint(field)
    #
    #         if fields["/T"] == '(Check Box7)':
    #             fields.update(pdfrw.PdfDict(V="/n"))
    #     pdfrw.PdfWriter().write(outputStream, template)

    def merge_pdf_form(self):
        new_pdf = PdfFileReader("output.pdf")
        # read your existing PDF
        existing_pdf = PdfFileReader(open("LPA_form.pdf", "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        print(existing_pdf.getNumPages())
        print(self.generated_pages)
        for i in range(0, existing_pdf.getNumPages()):
            page = existing_pdf.getPage(i)
            if i in self.generated_pages:
                pageNum = self.generated_pages.index(i)
                page.mergePage(new_pdf.getPage(pageNum))
            output.addPage(page)
        # finally, write "output" to a real file
        outputStream = open("merged_APL_form.pdf", "wb")
        output.write(outputStream)
        outputStream.close()

    def generate_canvas(self):
        self.set_check_box().set_text_box()
        self.c.save()

    def get_generated_pdf(self):
        pages = self.get_pages()
        i = 0
        for page in pages:
            if self.fields_on_page_exists(page):
                self.generate_page(page)
                self.c.showPage()
                self.generated_pages.append(i)
            i += 1
        self.generate_canvas()
        self.merge_pdf_form()


if __name__ == "__main__":
    # os.remove("myOutputPdf.pdf")
    #os.remove("output.pdf")
    # create_APL_form()
    # write_fillable_pdf("APL_form27.pdf", "output.pdf")
    # get_fillable_fields()
    LPAFormFill().get_generated_pdf()

#merge pdfs
#
# from PyPDF2 import PdfFileWriter, PdfFileReader
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
#
# packet = io.BytesIO()
# # create a new PDF with Reportlab
# can = canvas.Canvas(packet, pagesize=letter)
# can.drawString(10, 100, "Hello world")
# can.save()
#
# #move to the beginning of the StringIO buffer
# packet.seek(0)
# new_pdf = PdfFileReader("output.pdf")
# # read your existing PDF
# existing_pdf = PdfFileReader(open("LPA_form.pdf", "rb"))
# output = PdfFileWriter()
# # add the "watermark" (which is the new pdf) on the existing page
# for i in range(1, existing_pdf.getNumPages()):
#     page = existing_pdf.getPage(i)
#     if i - 1 < new_pdf.getNumPages():
#         page.mergePage(new_pdf.getPage(i - 1))
#     output.addPage(page)
# # finally, write "output" to a real file
# outputStream = open("merged_APL_form.pdf", "wb")
# output.write(outputStream)
# outputStream.close()
