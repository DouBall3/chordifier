# Chordifier
###### Chord translator for akordovnik

Chordifier is simple python script which takes input file in `*.chord` format and translate it to php file suitable for akordovnik application.

# Usage
```sh
$ python3 chordifier.py <in.chord> <out.php>
```

### Example of chord file

```
Sraž nás na kolena
Škwor
R:
|G#m|Sraž nás na kolena
|H|výhružka s náma nic neudělá
tak|C#|dál konec svejch dnů
hle|G#m\dám
R
1.
Zkou|H\šej jít dál tou naší
duší|C#|závislou
nej|H\si v tom sám i ostatní v
tom s|C#|námi jsou
2.
Až|H|ke hvězdám jak silný
tady|C#|zůstanou
a|H|já se ptám co pro nás
bude|C#|záchranou
co pro nás bude záchranou
R
3.
Když|H|dojde nám
zlý časy se tu|C#|rýsujou
tu|H|sílu znám
a v mozku myši|C#|fízlujou
a v mozku myši fízlujou
-()-
R
R
```

### Example of output
```php
<?php
array_push($names,"Sraž nás na kolena
");
array_push($authors,"Škwor
");
array_push($songs,'<br /><span class="verse">R:</span><br /><sup class="chord">G#m</sup> Sraž nás na kolena<br /><sup class="chord">H</sup> výhružka s náma nic neudělá<br />tak<sup class="chord">C#</sup> dál konec svejch dnů<br />hle<sup class="chord">G#m</sup>dám<br /><br /><span class="verse">R:</span><br /><br /><span class="verse">1:</span><br />Zkou<sup class="chord">H</sup>šej jít dál tou naší<br />duší<sup class="chord">C#</sup> závislou<br />nej<sup class="chord">H</sup>si v tom sám i ostatní v<br />tom s<sup class="chord">C#</sup> námi jsou<br /><br /><span class="verse">2:</span><br />Až<sup class="chord">H</sup> ke hvězdám jak silný<br />tady<sup class="chord">C#</sup> zůstanou<br />a<sup class="chord">H</sup> já se ptám co pro nás<br />bude<sup class="chord">C#</sup> záchranou<br />co pro nás bude záchranou<br /><br /><span class="verse">R:</span><br /><br /><span class="verse">3:</span><br />Když<sup class="chord">H</sup> dojde nám<br />zlý časy se tu<sup class="chord">C#</sup> rýsujou<br />tu<sup class="chord">H</sup> sílu znám<br />a v mozku myši<sup class="chord">C#</sup> fízlujou<br />a v mozku myši fízlujou<br /><br /><span class="verse">~mezihra~</span><br /><br /><span class="verse">R:</span><br /><br /><span class="verse">R:</span><br />');
$chords = ['G#m','H','C#','<br />'];
```

