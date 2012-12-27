for i in `seq 1900 2011`;
do
	curl --data "top=1000&year=$i&number=n&submit=%20%20Go%20%20" 'http://www.socialsecurity.gov/cgi-bin/popularnames.cgi' > $i.html ;
done
