mkdir libs
pip install -r requirements.txt -t ./libs/
cd libs	&& zip -r ../libs.zip .
cd ../ && rm -r libs