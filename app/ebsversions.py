import sys
import boto3


def ebs_utils_main(args):
    if args.__len__() > 0:
        methodname = eval(args[0])
        methodname(args[1:])
    else:
        print('Please provide the parameters')


def remove_ebs_versions(parameters):
        keep_latest = int(parameters[0])
        ebs_client = boto3.client('elasticbeanstalk')
        ebsapps = ebs_client.describe_applications()
        apps = ebsapps['Applications']
        for app in apps:
            ebs_application = app['ApplicationName']
            if ebs_application.startswith('ds-'):
                if 'Versions' in app:
                    ebs_versions = sorted(app['Versions'], reverse=True)
                    selected_versions = ebs_versions[keep_latest:]
                    for version in selected_versions:
                        ebs_client.delete_application_version(ApplicationName=ebs_application, VersionLabel=version, DeleteSourceBundle=False)
                        print("deleted", ebs_application, " version #", version)


if __name__ == "__main__":
    ebs_utils_main(sys.argv[1:])
