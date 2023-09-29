import re

meyveler = ["elma", "armut", "kiraz", "nar", "şeftali", "muz",
            "karpuz", "kavun", "kivi", "böğürtlen", "vişne", "karadut",
            "çilek", "kızılcık", "incir", "frenk üzümü", "ahududu"
            ]
pattern1 = "[a-zşöüşğıç ]{4,}"
pattern2 = "^k.*z$"
for meyve in meyveler:
    if re.fullmatch(pattern2, meyve):
        print(meyve)
