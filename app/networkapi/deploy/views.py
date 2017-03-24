from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework import authentication, permissions
from rest_framework.response import Response
from django.conf import settings

import requests


def get_jenkins_url(jenkins_url, env, staging_job, token):
    url = '{}/view/{}/job/{}/build?token={}&cause=Django+Admin+Trigger'
    return url.format(
        jenkins_url,
        env,
        staging_job,
        token
    )

staging_job_url = get_jenkins_url(
    settings.JENKINS_URL,
    'STAGING',
    settings.JENKINS_STAGING_JOB,
    settings.JENKINS_TOKEN
)

production_job_url = get_jenkins_url(
    settings.JENKINS_URL,
    'PROD',
    settings.JENKINS_PRODUCTION_JOB,
    settings.JENKINS_TOKEN
)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAdminUser])
def deployView(request, env, format=None):
    """
    Trigger a Jenkins deployment
    """

    if not request.user.has_perm('app.can_reboot_server'):
        return Response("Unauthorized", 401)

    if env == 'STAGING':
        r = requests.get(staging_job_url)
    else:
        r = requests.get(production_job_url)

    if r.status_code != 201:
        return Response('Failed to build', 400)

    return Response('Success', 201)
