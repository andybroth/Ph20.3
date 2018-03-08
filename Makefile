include config.mk

# all the python files
PY_FILES=$(wildcard *.py)

# all the plots
PLOTS=$(patsubst %.py, %.pdf, $(PY_FILES))

.PHONY : all
all : Ordinary_DifEQ.pdf

Ordinary_DifEQ.pdf : Ordinary_DifEQ.tex $(PLOTS) error_plot.pdf
	$(LATEX_EXE)

## pdfs      : Makes the pdf plots
.PHONY : pdfs
pdfs : $(PLOTS) error_plot.pdf

#python executable changed for CDW's machine
%.pdf : %.py
	~/anaconda3/bin/python3 $< 

## clean     : removes auto-generated files
.PHONY : clean
clean : 
	rm -f $(PLOTS)
	rm -f error_plot.pdf
	rm -f Ordinary_DifEQ.aux
	rm -f Ordinary_DifEQ.idx
	rm -f Ordinary_DifEQ.log
	rm -f Ordinary_DifEQ.out
	rm -f Ordinary_DifEQ.pdf

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
