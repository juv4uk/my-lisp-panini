# savarṇa для ṛ/ḷ (1.1.9 + vārttika) і 6.1.101: джерельний аудит, 2026-09-30

Read-only щодо `machine/`, `sastra/` і щодо shiva-sutras. Мета: закрити питання «чи ṛ і ḷ savarṇa і що дає 6.1.101» з цитатами.

## Що запускав / читав / не перевірив

- Запускав: `python3` проти `/home/agents/work/shiva-upc7/prototype` (`upc14v2.py`, `upc14v2_vowel_sandhi.py`, worktree на `work/44-upc14v2-graph-sonnet`): `g.savarna`, `g.dirgha`, `vowel_sandhi(l, r, vartika=False|True)` для чотирьох пар.
- Читав: реєстр 1.1.9, 1.1.10, 6.1.101; `KASIKA-1.1.9.yaml`, `KASIKA-1.1.10.yaml`, `KASIKA-6.1.101.yaml`; `kAshikAvRRitti.txt` рядки 53198, 53389, 53396.
- Не перевірив: шар [SCHOLARLY] (Cardona, Kiparsky); Siddhāntakaumudī і Mahābhāṣya на 1.1.9 (Source Ladder не пройдено далі Kāśikā); чи vārttika «ṛkāra-ḷkārayoḥ savarṇasañjñā» приписується Kātyāyana в самих цих джерелах (Kāśikā каже лише «vaktavyā»); txt-рядок для 1.1.9 не шукав.

## [PANINI] (сутри; реєстр)

- 1.1.9 `tulyAsyaprayatnaM savarRam`: два звуки savarṇa, якщо однакові місце вимови й зусилля (ābhyantara-prayatna). Сама сутра НЕ згадує ṛ і ḷ.
- 1.1.10 `nAjJalO`: голосний і приголосний не savarṇa.
- 6.1.101 `akaH savarRe dIrGaH`: ak + savarṇa ac → одна dīrgha (ekādeśa під 6.1.84).

## [TRADITION: Kāśikā, vārttika; НЕ сутра Паніні] (цитати)

- Kāśikā на 1.1.9: «ṛkāra-ḷkārayoḥ savarṇasañjñā vaktavyā / hotḷkāraḥ / hotṛkāraḥ / ubhayoḥ ṛvarṇasya ḷvarṇasya ca āntaratamaḥ savarṇo dīrgho nāsti iti ṛkāra eva dīrgho bhavati».
  Там само: «ḷ-varṇasya dīrghā na santi, taṃ dvādaśa-bhedam ācakṣate» (ḷ має 12 різновидів, довгого нема).
- Kāśikā на 6.1.101: «savarṇadīrghatve ṛti ṛ vā vacanam: ṛti savarṇe parabhūte tatra ṛ vā bhavati … hotṛ ṛkāraḥ hotṛkāraḥ; yadā na ṛ tadā dīrgha eva hotṝkāraḥ»; «lṛti lṛ vā: … hotṛ lṛkāraḥ hotlṛkāraḥ / hotṝkāraḥ»; «ṛkāralṛkārayoḥ savarṇāsañjñāvidhir uktaḥ / dīrghapakṣe tu samudāyāntaratamasya lṛvarṇasya dīrghasya abhāvāt ṛkāraḥ kriyate». txt:53389, 53396.
- Kāśikā (txt:53198, на іншій сутрі): «ṛkāralṛkārayoḥ sāvarṇyavidhiḥ iti ṛti iti lṛkāro 'pi gṛhyate»: той самий факт (ṛ і ḷ savarṇa за vārttika) використовується й тут.

## Висновок (мій; з цитат вище)

1. Без vārttika ṛ і ḷ НЕ savarṇa за 1.1.9 (місця різні: мурдханья vs дантья); тому 6.1.101 на пару ṛ/ḷ не діє. Це саме те, що каже граф за замовчуванням (`savarna(f, x) = False`).
2. З vārttika вони savarṇa; 6.1.101 дає результат-множину (варіанти через `vā`), а не один звук:

| ліворуч + праворуч | множина результатів | опора |
|---|---|---|
| ṛ + ṛ | {ṝ, ṛ} | «ṛti ṛ vā», hotṛkāraḥ / hotṝkāraḥ (Kāśikā 6.1.101) |
| ṛ + ḷ | {ṝ, ḷ} | «lṛti lṛ vā», hotlṛkāraḥ / hotṝkāraḥ (Kāśikā 6.1.101) |
| ḷ + ṛ | {ṝ, ṛ} | ЛИШЕ ВИСНОВОК за vārttika «ṛti savarṇe parabhūte ṛ vā»; прикладу в Kāśikā нема |
| ḷ + ḷ | {ṝ, ḷ} | ЛИШЕ ВИСНОВОК за «lṛti lṛ vā» + «ḷ довгого не має»; прикладу нема |

3. Довгий результат завжди ṝ, бо ḷ довгого не має (Kāśikā 1.1.9).

## [COMPUTATIONAL INTERPRETATION]: порівняння з реалізаціями (запуск)

- Граф UPC-14 v2 (`ffd8813`), `vowel_sandhi(..., vartika=True)`: ṛ+ṛ = ṝ, варіант ṛ; ṛ+ḷ = ṝ, варіант ḷ; ḷ+ṛ = ṝ, варіант ṛ; ḷ+ḷ = ṝ, варіант ḷ. Це ТОЧНО збігається з таблицею вище (включно з двома виведеними рядками). Без `vartika` ṛ+ḷ, ḷ+ṛ, ḷ+ḷ йдуть у 6.1.77 з позначкою «not attested in the Kasika», що відповідає цитатам: без vārttika 6.1.101 не діє, а Kāśikā 6.1.77 таких форм не наводить.
- Розбіжність у самій моделі: `g.dirgha(ḷ, ḷ)` кидає `GraphError` («ḷ has no long form»); але `vowel_sandhi` цей випадок обходить окремою гілкою vārttika, тож користувачеві видно коректний результат. Вхід через `dirgha` напряму лишається помилкою, це не суперечить Kāśikā (довгого ḷ нема), але й не дає ṝ.
- Мій `machine/derivation.lisp` (`savarṇa-pair?`): пари лише a/A, i/I, u/U, f/F; f+f → лише F (варіант ṛ відсутній); ḷ не представлений зовсім. Це НЕ відповідає таблиці; не виправлено (machine/ не чіпав без слова sdvova).

## [MY-LISP HYPOTHESIS]

Не додавав.

## Статус питання

Закрито на рівні Kāśikā для двох атестованих випадків (ṛ+ṛ, ṛ+ḷ), для двох інших (ḷ+ṛ, ḷ+ḷ) це висновок за симетрією vārttika, не атестований прикладом. Знахідку шіви про чотири випадки (ṛ+ṛ {ṝ,ṛ}; ṛ+ḷ {ṝ,ḷ}; ḷ+ṛ {ṝ,ṛ}; ḷ+ḷ {ṝ,ḷ}) підтверджено читанням Kāśikā, окрім двох виведених рядків. Не перевірено: Siddhāntakaumudī / Mahābhāṣya та шар SCHOLARLY.
