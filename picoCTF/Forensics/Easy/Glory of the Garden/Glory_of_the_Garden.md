# Glory of the Garden

![image.png](images/image.png)

We can first detect the file type and metadata.

```bash
└─$ file garden.jpg 
garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3

└─$ exiftool garden.jpg 
ExifTool Version Number         : 13.36
File Name                       : garden.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2025:11:14 14:58:29-05:00
File Access Date/Time           : 2026:02:03 10:50:07-05:00
File Inode Change Date/Time     : 2026:02:03 10:50:01-05:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Image Width                     : 2999
Image Height                    : 2249
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2999x2249
Megapixels                      : 6.7

```

I saw there is binary data, maybe we can try using the `-b` flag to extract them

```bash
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
```

However, it seems they are gibberish, and using strings will not extract useful data

```bash
└─$ exiftool -b garden.jpg                                                                                                                                                                                                                 
13.36garden.jpg.22951912025:11:14 14:58:29-05:002026:02:03 10:50:07-05:002026:02:03 10:50:01-05:00100664JPEGJPGimage/jpeg1 117272Lino528mntrRGB XYZ 1998:02:09 06:49:00acspMSFT0IEC sRGB0 000.9642 1 0.82491HP  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0Copyright (c) 1998 Hewlett-Packard CompanysRGB IEC61966-2.10.95045 1 1.089050 0 00.43607 0.22249 0.013920.38515 0.71687 0.097080.14307 0.06061 0.7141IEC http://www.iec.chIEC 61966-2.1 Default RGB colour space - sRGBReference Viewing Condition in IEC61966-2.119.6445 20.3718 16.80893.92889 4.07439 3.36179176.03647 80 87.1246210 0 000.009992CRT curv
%+28>ELRY`gnu|������������������������������
                              &/8AKT]gqz������������
+:IXgw��������'7HYj{�������+=Oat�������             !-8COZfr~���������� -;HUcq~���������
                                    �           %       :       O       d       y       �       �       �       �       �       �

'
=
T
j
�
�
�
�
�
�

 "
  9
   Q
    i
     �
      �
       �
        �
         �
          �

           *
            C
             \
              u
               �
                �
                 �
                  �
*R{���Gp���@j���>i���  A l � � �!!H!u!�!�!�"'"U"�"�"�#
(?(q(�(�))8)k)�)�**5*h*�*�++6+i+�+�,,9,n,�,�-▒'I'z'�'�(
3F33�3�4+4e4�4�55M5�5�5�676r6�6�7$7`7�7�88P8�8�99B99�9�:6:t:�:�;-;k;�;�<'<e<�<�="=a=�=�> >`>�>�?!?a?�?�@#@d@�@�A)AjA�A�B0BrB�B�C:C}C�DDGD�D�EEUE�E�F"FgF�F�G5G{G�HHKH�H�IIcI�I�J7J}J�K
                                                                                                                                                                                      KSK�K�L*LrL�MMJM�M�N%NnN�OOIO�O�P'PqP�QQPQ�Q�R1R|R�SS_S�S�TBT�T�U(UuU�VV\V�V�WDW�W�X/X}X�Y▒YiY�ZZVZ�Z�[E[�[�\5\�\�]']x]�^▒^l^�__a_�``W`�`�aOa�a�bIb�b�cCc�c�d@d�d�e=e�e�f=f�f�g=g�g�h?h�h�iCi�i�jHj�j�kOk�k�lWl�m`m�nnkn�ooxo�p+p�p�q:q�q�rKr�ss]s�ttpt�u(u�u�v>v�v�wVw�xxnx�y*y�y�zFz�{{c{�|!|�|�}A}�~~b~�#���G���
�k�0�����W��������G����r�;����i�Ή3�����d�ʋ0�����c�ʍ1�����f�Ώ6����n�?����z���M��� �����_�ɖ4���
�u���L���$�����h�՛B��������d�Ҟ@��������i�ءG���&����v���V�ǥ8���▒�����n���R�ĩ7�������u���\�ЭD���-�������u���`�K�³8���%�������y���h���Y�ѹJ�º;���.���!������
������2���F���[���p��������(���@���X���r��������4���P���m��������8���W���w����)���K���m��curvd���l���v��ۀ�܊�ݖ�ޢ�)�6���D���S���c���s�����
%+28>ELRY`gnu|������������������������������
                              &/8AKT]gqz������������
+:IXgw��������'7HYj{�������+=Oat�������             !-8COZfr~���������� -;HUcq~���������
                                    �           %       :       O       d       y       �       �       �       �       �       �

'
=
T
j
�
�
�
�
�
�

 "
  9
   Q
    i
     �
      �
       �
        �
         �
          �

           *
            C
             \
              u
               �
                �
                 �
                  �
�.Id����        %A^z����        &Ca~����1Om����&Ed����#Cc����'Ij����4Vx���&Il����Ae����▒▒@▒e▒�▒�▒�▒� Ek���▒▒*▒Q▒w▒�▒�▒�

*R{���Gp���@j���>i���  A l � � �!!H!u!�!�!�"'"U"�"�"�#
(?(q(�(�))8)k)�)�**5*h*�*�++6+i+�+�,,9,n,�,�-▒'I'z'�'�(
3F33�3�4+4e4�4�55M5�5�5�676r6�6�7$7`7�7�88P8�8�99B99�9�:6:t:�:�;-;k;�;�<'<e<�<�="=a=�=�> >`>�>�?!?a?�?�@#@d@�@�A)AjA�A�B0BrB�B�C:C}C�DDGD�D�EEUE�E�F"FgF�F�G5G{G�HHKH�H�IIcI�I�J7J}J�K
                                                                                                                                                                                      KSK�K�L*LrL�MMJM�M�N%NnN�OOIO�O�P'PqP�QQPQ�Q�R1R|R�SS_S�S�TBT�T�U(UuU�VV\V�V�WDW�W�X/X}X�Y▒YiY�ZZVZ�Z�[E[�[�\5\�\�]']x]�^▒^l^�__a_�``W`�`�aOa�a�bIb�b�cCc�c�d@d�d�e=e�e�f=f�f�g=g�g�h?h�h�iCi�i�jHj�j�kOk�k�lWl�m`m�nnkn�ooxo�p+p�p�q:q�q�rKr�ss]s�ttpt�u(u�u�v>v�v�wVw�xxnx�y*y�y�zFz�{{c{�|!|�|�}A}�~~b~�#���G���
�k�0�����W��������G����r�;����i�Ή3�����d�ʋ0�����c�ʍ1�����f�Ώ6����n�?����z���M��� �����_�ɖ4���
�u���L���$�����h�՛B��������d�Ҟ@��������i�ءG���&����v���V�ǥ8���▒�����n���R�ĩ7�������u���\�ЭD���-�������u���`�K�³8���%�������y���h���Y�ѹJ�º;���.���!������
������2���F���[���p��������(���@���X���r��������4���P���m��������8���W���w����)���K���m��curvd���l���v��ۀ�܊�ݖ�ޢ�)�6���D���S���c���s�����
%+28>ELRY`gnu|������������������������������
                              &/8AKT]gqz������������
+:IXgw��������'7HYj{�������+=Oat�������             !-8COZfr~���������� -;HUcq~���������
                                    �           %       :       O       d       y       �       �       �       �       �       �

'
=
T
j
�
�
�
�
�
�

 "
  9
   Q
    i
     �
      �
       �
        �
         �
          �

           *
            C
             \
              u
               �
                �
                 �
                  �
�.Id����        %A^z����        &Ca~����1Om����&Ed����#Cc����'Ij����4Vx���&Il����Ae����▒▒@▒e▒�▒�▒�▒� Ek���▒▒*▒Q▒w▒�▒�▒�

*R{���Gp���@j���>i���  A l � � �!!H!u!�!�!�"'"U"�"�"�#
(?(q(�(�))8)k)�)�**5*h*�*�++6+i+�+�,,9,n,�,�-▒'I'z'�'�(
3F33�3�4+4e4�4�55M5�5�5�676r6�6�7$7`7�7�88P8�8�99B99�9�:6:t:�:�;-;k;�;�<'<e<�<�="=a=�=�> >`>�>�?!?a?�?�@#@d@�@�A)AjA�A�B0BrB�B�C:C}C�DDGD�D�EEUE�E�F"FgF�F�G5G{G�HHKH�H�IIcI�I�J7J}J�K
                                                                                                                                                                                      KSK�K�L*LrL�MMJM�M�N%NnN�OOIO�O�P'PqP�QQPQ�Q�R1R|R�SS_S�S�TBT�T�U(UuU�VV\V�V�WDW�W�X/X}X�Y▒YiY�ZZVZ�Z�[E[�[�\5\�\�]']x]�^▒^l^�__a_�``W`�`�aOa�a�bIb�b�cCc�c�d@d�d�e=e�e�f=f�f�g=g�g�h?h�h�iCi�i�jHj�j�kOk�k�lWl�m`m�nnkn�ooxo�p+p�p�q:q�q�rKr�ss]s�ttpt�u(u�u�v>v�v�wVw�xxnx�y*y�y�zFz�{{c{�|!|�|�}A}�~~b~�#���G���
�k�0�����W��������G����r�;����i�Ή3�����d�ʋ0�����c�ʍ1�����f�Ώ6����n�?����z���M��� �����_�ɖ4���
�u���L���$�����h�՛B��������d�Ҟ@��������i�ءG���&����v���V�ǥ8���▒�����n���R�ĩ7�������u���\�ЭD���-�������u���`�K�³8���%�������y���h���Y�ѹJ�º;���.���!������
������2���F���[���p��������(���@���X���r��������4���P���m��������8���W���w����)���K���m��299922490832 22999 22496.744751��S���c���s�����

```

Turns out that this challenge only need to use strings to solve

```bash
─$ strings garden.jpg|tail
h--@3
cZi-
M(.I
]hWP&
jc#k
=7g&
mjx/
s\]|."Ue
\qZf
Here is a flag: picoCTF{more_than_m33ts_the_3y339140129}
```

Flag: `picoCTF{more_than_m33ts_the_3y339140129}`
