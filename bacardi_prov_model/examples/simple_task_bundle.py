# SPDX-FileCopyrightText: 2023 German Aerospace Center (DLR)
#
# SPDX-License-Identifier: MIT

"""Generates provenance bundle using the simplified task model"""

from pathlib import Path

import prov.model as prov

from bacardi_prov_model import utils, task


DOCUMENT_NAME = Path(__file__).name[:-3]
OUTPUT_PATH = Path.cwd() / Path("example-output") / Path(DOCUMENT_NAME)
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

##################################################################
# Instances of example records

# Bundles
TASK_BUNDLE_1 = 'task_bundle:1'

# Entities
DB_ENTRY_1 = 'db_entry:1'
DB_ENTRY_2 = 'db_entry:2'
PRODUCT_1 = 'product:1'
PRODUCT_2 = 'product:2'
TASK_CONFIG_1 = 'task_config:1'
TASK_RESULT_1 = 'task_log:1'
INP_1 = 'input:1'
OUT_1 = 'output:1'

# Activities
TASK_1 = 'task:1'

# Agents
BACARDI = 'agent:BACARDI'
GSOC = 'agent:GSOC'
SPACE_TRACK = 'agent:SPACE-TRACK'


def main():
    document = prov.ProvDocument(namespaces=task.NAMESPACES)

    # Agents
    document.agent(BACARDI, other_attributes=(
        (prov.PROV_TYPE, 'SoftwareAgent'),
    ))
    document.agent(GSOC, other_attributes=(
        (prov.PROV_TYPE, 'Organization'),
    ))
    document.agent(SPACE_TRACK, other_attributes=(
        (prov.PROV_TYPE, 'Organization'),
    ))

    #  Bundles
    b_task_1 = document.bundle(TASK_BUNDLE_1)

    # Entities
    b_task_1.entity(INP_1, other_attributes=(
        (prov.PROV_TYPE, prov.PROV_ATTR_COLLECTION),
        (prov.PROV_TYPE, task.TYPE.INPUT),
    ))
    b_task_1.entity(OUT_1, other_attributes=(
        (prov.PROV_TYPE, prov.PROV_ATTR_COLLECTION),
        (prov.PROV_TYPE, task.TYPE.OUTPUT),
    ))
    b_task_1.entity(TASK_CONFIG_1, other_attributes=(
        (prov.PROV_TYPE, task.TYPE.TASK_CONFIGURATION),
    ))
    b_task_1.entity(TASK_RESULT_1, other_attributes=(
        (prov.PROV_TYPE, task.TYPE.TASK_LOG),
    ))
    b_task_1.entity(DB_ENTRY_1, other_attributes=(
        (prov.PROV_TYPE, task.TYPE.DB_ENTRY),
    ))
    b_task_1.entity(DB_ENTRY_2, other_attributes=(
        (prov.PROV_TYPE, task.TYPE.DB_ENTRY),
    ))
    b_task_1.entity(PRODUCT_1, other_attributes=(
        (prov.PROV_TYPE, task.TYPE.PRODUCT),
    ))
    b_task_1.entity(PRODUCT_2, other_attributes=(
        (prov.PROV_TYPE, task.TYPE.PRODUCT),
    ))

    # Activities
    b_task_1.activity(TASK_1, other_attributes=(
        (prov.PROV_TYPE, task.TYPE.TASK),
    ))

    # Relations
    b_task_1.wasAssociatedWith(TASK_1, BACARDI)
    b_task_1.wasAttributedTo(PRODUCT_1, SPACE_TRACK, None, None)
    b_task_1.wasAttributedTo(PRODUCT_2, GSOC, None, None)

    b_task_1.hadMember(INP_1, PRODUCT_1)
    b_task_1.hadMember(INP_1, DB_ENTRY_1)
    b_task_1.hadMember(INP_1, TASK_CONFIG_1)
    b_task_1.used(TASK_1, INP_1, None, None)

    b_task_1.hadMember(OUT_1, TASK_RESULT_1)
    b_task_1.hadMember(OUT_1, DB_ENTRY_2)
    b_task_1.hadMember(OUT_1, PRODUCT_2)
    b_task_1.wasGeneratedBy(OUT_1, TASK_1)

    # Output
    document.serialize(destination=f'{OUTPUT_PATH}/{DOCUMENT_NAME}.ttl', format='rdf')
    document.serialize(destination=f'{OUTPUT_PATH}/{DOCUMENT_NAME}.provn', format='provn')
    document.serialize(destination=f'{OUTPUT_PATH}/{DOCUMENT_NAME}.json', format='json', indent=2)
    document.serialize(destination=f'{OUTPUT_PATH}/{DOCUMENT_NAME}.xml', format='xml')
    utils.render(document, f'{OUTPUT_PATH}/{DOCUMENT_NAME}.svg', 'svg')
    utils.render(document, f'{OUTPUT_PATH}/{DOCUMENT_NAME}.pdf', 'pdf')


if __name__ == '__main__':
    main()
