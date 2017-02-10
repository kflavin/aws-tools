#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print "Please provide the filename to read."
    sys.exit(1)
else:
    f_params = sys.argv[1]

def run():
    with open(f_params, "r") as f:
        params = f.read()

    print "aws --profile <profile> cloudformation create-stack --disable-rollback --stack-name <stackname> --template-body <file://...> --parameters",

    for param in params.strip().split("\n"):
        key = param.split()[0]
        value = " ".join(param.split()[1:])
        if value.find(" ") >= 0:
            value = '"{surround}"'.format(surround=value)
        print "ParameterKey={key},ParameterValue={value}".format(key=key, value=value),


if __name__ == '__main__':
    run()
