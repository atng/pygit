import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import blue, black, white
import pdfrw


ANNOTATIONS_KEY = "/Annots"

def personalDetails(c, form):
    c.drawString(10, 650, "Full name as in ID")
    form.textfield(name="fname", tooltip="Full Name",
                   x=250, y=635, borderStyle="inset",
                   width=400,
                   textColor=black, forceBorder=True)

    c.drawString(250, 600, "ID number")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=350, y=585, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 550, "Country of issue")
    form.textfield(name="country", tooltip="country",
                   x=110, y=550, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 550, "Date of birth (dd/mm/yyyy)")
    form.textfield(name="date", tooltip="date",
                   x=350, y=550, borderStyle="inset",
                   forceBorder=True)

def personalDetBox(c, form):
    c.drawString(10, 650, "Full name as in ID")
    form.textfield(name="fname", tooltip="Full Name",
                   x=110, y=635, borderStyle="inset",
                   borderColor=blue,
                   width=400,
                   textColor=black, forceBorder=True)

    c.drawString(250, 600, "ID number")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=350, y=585, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 550, "Country of issue")
    form.textfield(name="country", tooltip="country",
                   x=110, y=550, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 550, "Date of birth (dd/mm/yyyy)")
    form.textfield(name="date", tooltip="date",
                   x=350, y=535, borderStyle="inset",
                   forceBorder=True)
    c.drawString(110, 275, "Authorised to make decisions about(please tick one box only)")
    c.drawString(250, 250, "personal welfare only")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=250, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(250, 200, "property and affairs only")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=200, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(250, 150, "both personal welfare and property and affairs")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=150, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)


def personalDetBox2(c,form):
    c.drawString(10, 650, "Name of witness")
    form.textfield(name="witnam", tooltip="Name of witness",
                   x=110, y=635, borderStyle="inset",
                   width=400,
                   forceBorder=True)

    c.drawString(250, 600, "ID number")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=350, y=585, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 550, "Language/dialect translated in")
    form.textfield(name="dialect", tooltip="Language/dialect translated in",
                   x=350, y=535, borderStyle="inset",
                   forceBorder=True)

    c.drawString(110, 500, "Please tick box if translation of the contents of this instrument was given by the witness")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=500, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

# Creates form
def create_APL_form():
    c = canvas.Canvas("APL_form27.pdf")
    form = c.acroForm

    c.drawString(250, 150, "Please tick box if translator is certificate issuer")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=150, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    personalDetails(c, form)

    c.drawString(10, 450, "Name of translator")
    form.textfield(name="namt", tooltip="Name of translator",
                   x=110, y=450, borderStyle="inset",
                   width=400,
                   forceBorder=True)

    c.drawString(250, 400, "ID number")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=350, y=400, borderStyle="inset",
                   forceBorder=True)

    c.drawString(200, 350, "Language/dialect translated in")
    form.textfield(name="dialect", tooltip="Language/dialect translated in",
                   x=350, y=350, borderStyle="inset",
                   forceBorder=True)
    c.showPage()

    personalDetBox(c, form)

    c.showPage()

    personalDetBox2(c, form)

    c.drawString(10, 450, "Full name as in ID")
    form.textfield(name="fname", tooltip="Full Name",
                   x=110, y=450, borderStyle="inset",
                   borderColor=blue,
                   width=400,
                   textColor=black, forceBorder=True)

    c.drawString(250, 400, "ID number")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=350, y=400, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 350, "Country of issue")
    form.textfield(name="country", tooltip="country",
                   x=110, y=350, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 300, "Date of birth (dd/mm/yyyy)")
    form.textfield(name="date", tooltip="date",
                   x=350, y=300, borderStyle="inset",
                   forceBorder=True)
    c.drawString(110, 250, "Authorised to make decisions about(please tick one box only)")
    c.drawString(250, 250, "personal welfare only")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=250, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(250, 200, "property and affairs only")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=200, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(250, 150, "both personal welfare and property and affairs")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=150, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(10, 100, "Name of witness")
    form.textfield(name="witnam", tooltip="Name of witness",
                   x=110, y=100, borderStyle="inset",
                   width=400,
                   forceBorder=True)

    c.drawString(250, 50, "ID number")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=350, y=50, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 25, "Language/dialect translated in")
    form.textfield(name="dialect", tooltip="Language/dialect translated in",
                   x=350, y=25, borderStyle="inset",
                   forceBorder=True)

    c.drawString(110, 25, "Please tick box if translation of the contents of this instrument was given by the witness")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=25, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.showPage()

    personalDetails(c, form)
    c.drawString(110, 500, "Replacement donee is to replace (please tick one box only)")
    c.drawString(250, 450, "any donee that needs replacing")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=450, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(250, 400, "any personal welfare donee that needs replacing")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=400, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(250, 350, "any property and affairs donee that needs replacing")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=350, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(250, 300, "this named donee:")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=300, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    form.textfield(name="witnam", tooltip="Name of witness",
                   x=300, y=300, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 250, "Name of witness")
    form.textfield(name="witnam", tooltip="Name of witness",
                   x=110, y= 250, borderStyle="inset",
                   width=400,
                   forceBorder=True)

    c.drawString(250, 200, "ID number")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=350, y=200, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 150, "Language/dialect translated in")
    form.textfield(name="dialect", tooltip="Language/dialect translated in",
                   x=350, y=150, borderStyle="inset",
                   forceBorder=True)

    c.drawString(110, 100, "Please tick box if translation of the contents of this instrument was given by the witness")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=100, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)


    c.showPage()

    c.drawString(10, 700, "My donee shall have the authority to make decisions in all matters relating to my personal welfare, where I (the donor) no longer have the mental capacity to make such decisions:")
    c.drawString(155, 650, "Yes")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=650, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)
    c.drawString(345, 650, "No")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=300, y=650, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(110, 600, 'If "Yes" then:')
    c.drawString(115, 550, "b. My donee's authority shall extend to giving or refusing consent to the carrying out or continuation of treatment, including the conduct of a clinical trial, by a person provining health care for me:")
    c.drawString(155, 500, "Yes")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=500, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)
    c.drawString(345, 500, "No")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=300, y=500, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(115, 450, "c.Where there is more than 1 donee, they shall act (please tick one box only):")
    c.drawString(155, 400, "Jointly")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=400, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)
    c.drawString(155, 350, "Jointly and severally")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=350, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(10, 340, "My donee shall have the authority to make decisions in all matters relating to my property and affairs, where I (the donor) no longer have the mental capacity to make such decisions:")
    c.drawString(155, 320, "Yes")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=320, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)
    c.drawString(345, 320, "No")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=300, y=320, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(110, 300, "If 'Yes' then:")
    c.drawString(115, 280, "b. The following restrictions apply (please tick box below if applicable):")
    c.drawString(150, 250, "My donee shall not sell, transfer, convey, mortgage or charge my residential property at")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=250, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(115, 230, "c. My donee shall have the authority to dispose of my property by making gifts of cash on my behalf subject to section 14(3) and (4) of the Act (please tick one box only):")
    c.drawString(150, 215, "No")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=215, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)
    c.drawString(150, 200, "Yes, and the value of cash gifts is unrestricted")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=200, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)
    c.drawString(150, 185, "Yes, but the total value of cash gifts shall not exceed $")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=185, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)
    c.drawString(500, 170, "within 1 calendar year")
    form.textfield(name="fname", tooltip="Full Name",
                   x=400, y=150, borderStyle="inset",
                   textColor=black, forceBorder=True)

    c.drawString(115, 155, "d. Where there is more than 1 donee, they shall act (please tick one box only):")
    c.drawString(150, 140, "Jointly")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=140, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)
    c.drawString(150, 125, "Jointly and severally")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=125, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)
    c.showPage()

    c.showPage()

    c.drawString(10, 650, "Full name as in ID")
    form.textfield(name="fname", tooltip="Full Name",
                   x=110, y=635, borderStyle="inset",
                   width=400,
                   textColor=black, forceBorder=True)

    c.drawString(10, 600, "MCR/NRIC number")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=585, borderStyle="inset",
                   width=400,
                   forceBorder=True)

    c.drawString(10, 550, "Name of clinic/legal practice")
    form.textfield(name="country", tooltip="country",
                   x=110, y=550, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 550, "Contact number")
    form.textfield(name="date", tooltip="date",
                   x=350, y=550, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 500, "I am (please tick one box only)")
    c.drawString(110, 450, "a medical practicioner who is accredited by the Public Guardian to issue LPA")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=450, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(110, 400, "Please tick box if translation of the contents of this instrument was given by the witness")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=400, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(110, 350, "Please tick box if translation of the contents of this instrument was given by the witness")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=350, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.showPage()

    c.drawString(10, 600, "Date of this application")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=585, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 550, "Full name as in ID")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=535, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 500, "Contact number (home)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=485, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 450, "Contact number (office)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=250, y=435, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 400, "Contact number (mobile)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=385, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 350, "Email address")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=250, y=335, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 300, "Address")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=285, borderStyle="inset",
                   width=400,
                   forceBorder=True)
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=285, borderStyle="inset",
                   width=400,
                   forceBorder=True)

    c.drawString(10, 250, "Full name as in ID")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=250, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 200, "Contact number (home)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=200, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 150, "Contact number (office)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=250, y=150, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 100, "Contact number (mobile)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=100, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 75, "Email address")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=250, y=75, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 50, "Address")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=50, borderStyle="inset",
                   width=400,
                   forceBorder=True)
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=25, borderStyle="inset",
                   width=400,
                   forceBorder=True)

    c.showPage()

    c.drawString(10, 550, "Full name as in ID")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=535, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 500, "Contact number (home)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=485, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 450, "Contact number (office)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=250, y=435, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 400, "Contact number (mobile)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=385, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 350, "Email address")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=250, y=335, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 300, "Address")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=285, borderStyle="inset",
                   width=400,
                   forceBorder=True)
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=255, borderStyle="inset",
                   width=400,
                   forceBorder=True)

    c.drawString(110, 250, "Relationship to donor")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=250, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 200, "Full name as in ID")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=200, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 150, "Contact number (home)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=150, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 100, "Contact number (office)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=250, y=100, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 80, "Contact number (mobile)")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=80, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 80, "Email address")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=250, y=80, borderStyle="inset",
                   forceBorder=True)

    c.drawString(250, 60, "Address")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=60, borderStyle="inset",
                   width=400,
                   forceBorder=True)
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=40, borderStyle="inset",
                   width=400,
                   forceBorder=True)

    c.showPage()

    c.drawString(110, 650, "Please send the registered LPA by AR Registered Post to the following address:")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=635, borderStyle="inset",
                   forceBorder=True)
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=600, borderStyle="inset",
                   forceBorder=True)

    c.drawString(110, 500, "I am/ We are the (please tick one box only)")
    c.drawString(150, 450, "Donor")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=110, y=450, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(300, 450, "Donee")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=250, y=450, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(400, 450, "Donees (Donees who are required to act jointly must all join in the application)")
    form.checkbox(name="cb1", tooltip="Field cb1",
                  x=350, y=450, buttonStyle="check",
                  borderColor=black, fillColor=white,
                  textColor=black, forceBorder=True)

    c.drawString(110, 400, "Name of applicant(s)")

    c.drawString(10, 350, "1")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=350, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 300, "2")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=300, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 250, "3")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=250, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 200, "4")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=200, borderStyle="inset",
                   forceBorder=True)

    c.drawString(10, 150, "5")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=110, y=150, borderStyle="inset",
                   forceBorder=True)

    c.drawString(400, 400, "Date signed")
    form.textfield(name="IDnum", tooltip="ID number",
                   x=400, y=350, borderStyle="inset",
                   forceBorder=True)

    form.textfield(name="IDnum", tooltip="ID number",
                   x=400, y=300, borderStyle="inset",
                   forceBorder=True)

    form.textfield(name="IDnum", tooltip="ID number",
                   x=400, y=250, borderStyle="inset",
                   forceBorder=True)

    form.textfield(name="IDnum", tooltip="ID number",
                   x=400, y=200, borderStyle="inset",
                   forceBorder=True)

    form.textfield(name="IDnum", tooltip="ID number",
                   x=400, y=150, borderStyle="inset",
                   forceBorder=True)


    c.save()






# Fills in form
def write_fillable_pdf(input_pdf_path, output_pdf_path):
   template_pdf = pdfrw.PdfReader(input_pdf_path)
   for page in template_pdf.pages:
       annotations = page[ANNOTATIONS_KEY]
       data = ["Mike Driscoll", "123 Greenway Road", "Everytown", "IA", "Monica Geller", "162575", "English", "Phoebe Buffay", "76327672", "Singapore", "02/09/1985", "Joey Tribbiani", "7343", "German", "Chandler Bing", "83794", "Brazil", "23232", "Rachel Green", "74673", "Japanese", "Ross Geller", "47376", "France", "47563", "Ben Geller", "Gunther", "4687637", "Korean", "my stepfather", "Janice", "127218", "Clinic", "89384", "9199", "Jill Green", "23428", "387872", "79487", "email", "Address 1", "Address 2", "Emily Waltham", "74665", "874879", "92883", "other email", "Address 1", "Address 2", "mother", "Paul Stevens", "98747", "94878", "87973", "email", "Address 1", "Address 2", "brother", "Jack Geller", "329", "72893", "3879", "email", "Address 1", "Address 2", "Address line 1", "Address line 2", "Jennifer Aniston", "Courteney Cox", "Matthew Perry", "Matt LeBlanc", "Phoebe Buffay", "97283", "9877", "9787", "977", "9723987",   ]
       i = -1
       if annotations is not None:
           for annotation in annotations:
               if (i < len(data)):
                   annotation.update(
                       pdfrw.PdfDict(V="{}".format(data[i]))
                   )
                   i = i + 1
   pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

if __name__ == "__main__":
    #os.remove("APL_form27.pdf")
    #os.remove("output.pdf")
    create_APL_form()
    write_fillable_pdf("APL_form27.pdf", "output.pdf")


#merge pdfs

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 100, "Hello world")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader("output.pdf")
# read your existing PDF
existing_pdf = PdfFileReader(open("LPA_form.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
for i in range (1, existing_pdf.getNumPages()):
    page = existing_pdf.getPage(i)
    if i - 1 < new_pdf.getNumPages():
        page.mergePage(new_pdf.getPage(i-1))
    output.addPage(page)
# finally, write "output" to a real file
outputStream = open("merged_APL_form.pdf", "wb")
output.write(outputStream)
outputStream.close()
