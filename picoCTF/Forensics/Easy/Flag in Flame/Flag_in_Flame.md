# Flag in Flame

![image.png](images/image.png)

This is a txt file with a very long text

```bash
└─$ file logs.txt 
logs.txt: ASCII text, with very long lines (65536), with no line terminators

└─$ cat logs.txt |wc
      0       1 1592368
```

Here is just the first part of the log:

```bash
iVBORw0KGgoAAAANSUhEUgAAA4AAAASACAIAAAAh8bSOAAEAAElEQVR4nOz919MsyZUniP3OcY+IFJ+6ouqWBqoautDYRmN6emfaZmlc0mi2+7xPNJJ/GJ/4RvJtH5dmQ1vbHu4Mp9kzjQYGohuoAkrh1tWfysyIcPdz+HAiIj3Vp66oanHs2nczIyM8XB4t6PUP/i8ASEEDKKkqiQJQtgsgIjBUNWoUESJ1zjkiVUUiZibyIhIiVNWPpuPxuJxMiqI4OTt59uxZVTIRUaxDCJTaw8NDUpnNZm1d13Xt3ej27dvT6f58Pm8R67r2oze/+93vFuPXFovFuNQQQhEf/vVf//Xs4ScKrVA5dlHKcTH+7374f5xOpx+d/PoXv/jFA/mthyd3pqoAABDWYe+Nb/3pn/7ptLz9ySef/O1//rfkHKRhZr//7R//+Mee+ZNPPvnis18w80/++C++853v/OLXP//pT39ahCcAhEtV/fa/+j+8//77jPRv/+2/lQe/9s6zzAGcY+SLglJjb2dmVRIRImJmVSw/C4kIMxdF8cGf/TdvvPHGsy+/+NnPfianT733FBcKFeK1nhMxAFbYugAAJQAikYiSQFS8q0TEFeMQgir/6I9/dPvtHywWi9/85//5/Py8qPy8npdvfucHP/jBwXTyi1/8YvH5L0MI06pq23ame+//0R99+0d/2jTNlx//7W9/+1tqn5W+jFrGFMUf/Vf/8l++/60P27b9u7/99x
```

It looks like a base64 encode string, what if we decode it:

```bash
└─$ cat logs.txt |base64 -d|head
�PNG
▒
IHDR�!���IDATx�����,ɕ'���q��������▒���Fczzg�fi\�h���O4�▒��F�m�fC[��
                                                                   ��3��J��՟�p�s�p""=է��jq��w3##<\-���/HA(�*�P�
                                                                                                                "0T5j"u�9"UE"f&�""TՏ�����L��89;y��YU2Q�����CR��fm]�u���������|>o����7�������Ÿ�B��_����'
�P9vQ�q1��~��N����������'w���a��o����鴼��'�������af�����Ǟ��O>���_0�O��/�������?��OZ�'�KU����?������o������γ��c䋂RcogfU"bfU,?
                                                                                                                            3E����7o��Ƴ/����~&�O��
ⵞ1Vغ%"���@T��D���*���t��,��������������o~�?���t��_�b��/Ӫj�v�{���}�G�4��o�[j����Z���W��_���۶��������U<SU��
Q�"���{�x�[��������_�y���;w�����X$���G���k��V�����'O����[�ڶ}��YY�GGGι���mk��▒����7�|�[Ϟ={���x<>::RէO������ߖ�����}������g�}v����g�4�
��:b�~
��$��3����@m������>�`�������/�2q�MT�����w����>��������N��~װt���(��p��?���߼7�����_�⯈ف�9EG��������y�4����������="z�����������~������`,8�X=�U{b3/ 
                                                                                                                                               @�H��>uE��ʩ�L����/�b��������M�PH����{���<�����_޻w���G�~����n߾������w���7��(��/���>�H��
1%b2�
     ���:��kXD�(��4%�#�����Ͽy�����������q�9WK��G`�%�
���{��k<���O^����o={�L�TUutp���??yzV�Ǯ,��������Ç����Wq�`�2�x���1��m}�����~��ۯ������X,<��?��Ϟ���0����*y"b�"2�o}�;��?��_|�ſ���q�-=��ʪJXQt{�zp��_��_�����~���~
                                                           n����*��bȱG>��]_P`�� w�����'�����������
                                                                                                  ��13�����o~�����g?��/g�R�ݩ�N��%"h���H ��s��������ۏ����������!񍈠�"rn�����������������1z-��[�ѿ��ugr���>�������<#��Ɣ��hZN�7�?TU���������mY��L1F���w�����˔�/��������vQ���O���������M�?~\8wrr"o����?,�������+"���pE-m�Truŕں2�v���s(��G�����-�����?�����LU'�5��=��O~��C������O�2I��XDԕ\R��88��^��?���o����������IS��T5b
                                                                                                                                                                       ��h▒�D���?|��������??�?�η�������w�m��_���_��R�\�1��)ƽ;��~�m?9�
```

Great, it is a png file, we can recreate a png image with redirection (`cat logs.txt |base64 -d > flag.png`)

Opening the image, we can see a string:

![image.png](images/image%201.png)

If you think about the string, it ranges from 1-9, and A-F, which is probably a hex string. To solve this, we can write a python script to decode and chain them together for us:

```python
HexString=['70','69','63','6F','43','54','46','7B','66','6F','72','65','6E','73','69','63','73','5F','61','6E','61','6C','79','73','69','73','5F','69','73','5F','61','6D','61','7A','69','6E','67','5F','62','65','38','36','30'
          ,'32','37','39','7D']

print(''.join(chr(int(x,16)) for x in HexString))

```

Executing it will give us the flag

Flag: `picoCTF{forensics_analysis_is_amazing_be860279}`
