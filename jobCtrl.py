import json

import streamsets
import streamsets.sdk
from streamsets.sdk import *
from streamsets.sdk.config import *
from streamsets.sdk.examples import *
from streamsets.sdk.exceptions import *
from streamsets.sdk.models import *
from streamsets.sdk.sch import *
from streamsets.sdk.sch_api import *
from streamsets.sdk.sch_models import *
from streamsets.sdk.sdc import *
from streamsets.sdk.sdc_models import *
from streamsets.sdk.utils import *
from streamsets.sdk.constants import *

import warnings

warnings.filterwarnings("ignore")


class sch_job_ctrl:
    """
    StreamSets Python SDK job wrapper
    """

    __JOB = None
    __JOB_NAME = None
    __STATUS = None
    __CONTROL_HUB = None

    def __init__(self, control_hub, job_name):
        sch_job_ctrl.__CONTROL_HUB = control_hub
        sch_job_ctrl.__JOB_NAME = job_name
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )

    def get_start_time(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return (
            f"{datetime.fromtimestamp(sch_job_ctrl.__JOB.history[0].start_time/1000)}"
        )

    def get_finish_time(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return (
            f"{datetime.fromtimestamp(sch_job_ctrl.__JOB.history[0].finish_time/1000)}"
        )

    def get_all(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )

    def get_id(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )["id"]

    def get_status(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )["status"]

    def get_errorMessage(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )["errorMessage"]

    def get_errorInfos(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )["errorInfos"]

    def get_inputRecordCount(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )["inputRecordCount"]

    def get_outputRecordCount(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )["outputRecordCount"]

    def get_errorRecordCount(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )["errorRecordCount"]

    def get_color(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )["color"]

    def get_runCount(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return json.loads(
            sch_job_ctrl.__CONTROL_HUB.get_current_job_status(
                sch_job_ctrl.__JOB
            ).response.text
        )["runCount"]

    def get_metrics_run_count(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return (sch_job_ctrl.__JOB.metrics[0]).run_count

    def get_metrics_input_count(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return (sch_job_ctrl.__JOB.metrics[0]).input_count

    def get_metrics_output_count(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return (sch_job_ctrl.__JOB.metrics[0]).output_count

    def get_metrics_total_error_count(self):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        return (sch_job_ctrl.__JOB.metrics[0]).total_error_count

    def start_job(self, wait=False):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        sch_job_ctrl.__CONTROL_HUB.start_job(sch_job_ctrl.__JOB, wait=wait)
        return self.get_status()

    def wait_for_job_status(self, status, timeout_sec):
        sch_job_ctrl.__JOB = sch_job_ctrl.__CONTROL_HUB.jobs.get(
            job_name=sch_job_ctrl.__JOB_NAME
        )
        try:
            sch_job_ctrl.__CONTROL_HUB.wait_for_job_status(
                sch_job_ctrl.__JOB, status, timeout_sec=120 + timeout_sec
            )
        except:
            pass
        return self.get_status()