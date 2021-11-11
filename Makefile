PACKAGED_TEMPLATE = packaged.yaml
S3_BUCKET := $(S3_BUCKET)
TEMPLATE = template.yaml
APP_NAME 	 ?= bamboogooglesync

clean:
	rm -rf dist
	mkdir dist

build: clean
	cp -r bamboogooglesync requirements.txt dist/
	pip install -r requirements.txt --target dist/

package: build
	sam package --template-file $(TEMPLATE) --s3-bucket $(S3_BUCKET) --output-template-file $(PACKAGED_TEMPLATE)

deploy: package
	sam deploy --stack-name $(STACK_NAME) --template-file $(PACKAGED_TEMPLATE) --capabilities CAPABILITY_IAM