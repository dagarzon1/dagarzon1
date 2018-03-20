sample_1_*.png:sample_1_*.txt
	python DiegoGarzon_analysis.py 
sample_1_*.txt:
	python DiegoGarzon_generar.py 
clean:
	rm sample_1_*.txt
	rm sample_2_*.txt
