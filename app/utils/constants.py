from collections import namedtuple

Status = namedtuple('Status', ['PENDING', 'STARTED', 'SUCCESS', 'FAILURE', 'RETRY', 'REVOKED'])

statuses = Status(PENDING='PENDING', SUCCESS='SUCCESS', STARTED='STARTED', FAILURE='FAILURE',
                  RETRY='RETRY', REVOKED='REVOKED'
                  )
