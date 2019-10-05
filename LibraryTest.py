import fitz
import calendar
import sys
startyear = 2020

assert startyear.isdigit(), "year must be positive numeric"
startyear = int(startyear)
assert startyear > 0, "year must be positive numeric"
    
doc = fitz.open()
cal = calendar.LocaleTextCalendar(locale = "de")   # choose your locale
w, h = fitz.PaperSize("a4-l")                      # get sizes for A4 landscape paper

txt = cal.formatyear(startyear, m = 4)
doc.insertPage(-1, txt, fontsize = 12, fontname = "Courier", width = w, height = h)

txt = cal.formatyear(startyear + 1, m = 4)
doc.insertPage(-1, txt, fontsize = 12, fontname = "Courier", width = w, height = h)

txt = cal.formatyear(startyear + 2, m = 4)
doc.insertPage(-1, txt, fontsize = 12, fontname = "Courier", width = w, height = h)

doc.save("Kalender.pdf", garbage = 4, deflate = True)