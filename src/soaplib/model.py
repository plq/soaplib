# encoding: utf8
#
# Copyright © Burak Arslan <burak at arskom dot com dot tr>,
#             Arskom Ltd. http://www.arskom.com.tr
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#    3. Neither the name of the owner nor the names of its contributors may be
#       used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

from rpclib.model import ModelBase
from rpclib.model import SimpleModel

from rpclib.model.primitive import AnyXml
from rpclib.model.primitive import AnyDict
from rpclib.model.primitive import Unicode
from rpclib.model.primitive import _String
from rpclib.model.primitive import AnyUri
from rpclib.model.primitive import Decimal
from rpclib.model.primitive import Double
from rpclib.model.primitive import Float
from rpclib.model.primitive import Int
from rpclib.model.primitive import Integer
from rpclib.model.primitive import UnsignedInteger
from rpclib.model.primitive import UnsignedInteger64
from rpclib.model.primitive import UnsignedInteger32
from rpclib.model.primitive import UnsignedInteger16
from rpclib.model.primitive import UnsignedInteger8
from rpclib.model.primitive import Time
from rpclib.model.primitive import Date
from rpclib.model.primitive import DateTime
from rpclib.model.primitive import Duration
from rpclib.model.primitive import Boolean
from rpclib.model.primitive import Mandatory

from rpclib.model.binary import ByteArray

from rpclib.model.complex import ComplexModel
from rpclib.model.complex import XMLAttribute as XmlAttribute
from rpclib.model.complex import Array
from rpclib.model.complex import Iterable

from rpclib.model.enum import Enum

from rpclib.model.fault import Fault

from rpclib.model.table import TableModelMeta
from rpclib.model.table import TableModel
