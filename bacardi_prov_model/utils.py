# SPDX-FileCopyrightText: 2023 German Aerospace Center (DLR)
#
# SPDX-License-Identifier: MIT

from prov.dot import prov_to_dot


def render(document, path, fmt):
    dot = prov_to_dot(document)
    dot.write(path=path, format=fmt)
