# SPDX-FileCopyrightText: 2023 German Aerospace Center (DLR)
#
# SPDX-License-Identifier: MIT

"""Task Model"""
from prov.identifier import Namespace

NAMESPACES = [
    # Global bacardi namespace
    Namespace('task_type', 'https://bacardi.dlr.de/prov/ns/task/type/#'),
    Namespace('task_role', 'https://bacardi.dlr.de/prov/ns/task/role/#'),
    Namespace('task_attr', 'https://bacardi.dlr.de/prov/ns/task/attribute/#'),

    # Resource urls
    Namespace('agent', 'https://bacardi.dlr.de/prov/agent/'),
    Namespace('task_bundle', 'https://bacardi.dlr.de/prov/entity/TaskBundle/'),
    Namespace('task', 'https://bacardi.dlr.de/prov/activity/Task/'),
    Namespace('task_config', 'https://bacardi.dlr.de/prov/entity/TaskConfiguration/'),
    Namespace('task_log', 'https://bacardi.dlr.de/prov/entity/TaskLog/'),
    Namespace('input', 'https://bacardi.dlr.de/prov/entity/Input/'),
    Namespace('output', 'https://bacardi.dlr.de/prov/entity/Output/'),
    Namespace('db_entry', 'https://bacardi.dlr.de/prov/entity/DbEntry/'),
    Namespace('product', 'https://bacardi.dlr.de/prov/entity/Product/')
]


class TYPE:
    TASK_BUNDLE = 'task_type:TaskBundle'
    TASK_CONFIGURATION = 'task_type:TaskConfiguration'
    TASK_LOG = 'task_type:TaskLog'
    INPUT = 'task_type:Input'
    OUTPUT = 'task_type:Output'
    DB_ENTRY = 'task_type:DbEntry'
    PRODUCT = 'task_type:Product'
    TASK = 'task_type:Task'


class ATTRIBUTE:
    DB_MODEL = 'task_attr:DbModel'
    TASK_ID = 'task_attr:TaskId'
    DAG_ID = 'task_attr:DagId'
    PARENT_TASK_NAME = 'task_attr:ParentTaskName'
