# Indian History: real images for story cards

Status 2026-11-07 · Original documentary-image plan below. A separate draft pass now has 199 saved assets (189 generated interpretations, 10 licensed source assets) and 32 cover candidates. Contextual substitutions and limitations are recorded in `docs/research/indian-history-generation-queue.json`. Review gallery: `output/imagegen/indian-history/all-images.html`. No images have been integrated into lessons or published; documentary acquisition and historical/Assamese review are not claimed complete.

## Why

Of 294 story cards in `ih-01`–`ih-33`, **221 use a generic icon** (`scroll`, `seal`, `court`, `houses`, `embassy`, `calendar`, `door`) or a chip-grid `diagram`. The other 73 already use a map or a drawn figure and stay as they are. No card shows a real picture. Every lesson cover is one of eight shared era tiles.

A real object, site, document or period photograph turns a card into evidence the learner can look at, which is what the course promises.

## Rules for every image

- **Source:** Wikimedia Commons or museum open-access collections, public domain or CC BY/BY-SA. Record title, author, licence and URL per file in `docs/research/indian-history-images.md` (create it). Do not copy anything with unclear rights.
- **Evidence first:** prefer the object itself (seal, coin, inscription, manuscript, monument) or a period photograph. Later paintings and statues are allowed only with a "later depiction" caption.
- **Generated art:** the Assam History library has generated sheets of Xuanzang, Harsha and Aurangzeb. Use them only where marked, with the artist's-interpretation credit. They are not evidence.
- **Format:** WebP about 1080 px wide in `content/media/<lesson-id>/`; `build.py` makes `@480` copies. Use `imageCaption`, `imageLayout` and `imageKind` (`photo`, `document`, `diagram`) so the card shows a caption and credit.
- **Sensitive images:** violence (Jallianwala Bagh, Calcutta 1946) uses places or documents, never victims.
- **Do not change** card ids or text that exercises depend on. Adding `img` to a card that had `art` or `diagram` is safe.

## Priorities

- **A**: a well-known, freely licensed image clearly improves the card. Do these first.
- **B**: a good image exists, but it is weaker evidence or harder to license.
- **C**: no suitable image; keep the icon or chips.

Totals: **126 A**, **69 B**, **26 C** across 221 cards.

### ih-01-indus-cities · The Indus cities

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.02` | How old? | calendar | Dancing Girl bronze, Mohenjo-daro (National Museum, New Delhi) | artefact | A |
| `u2.01` | Drains under the street | houses | Covered brick drain on a Mohenjo-daro street | site photo | A |
| `u2.02` | The Great Bath | door | The Great Bath, Mohenjo-daro | site photo | A |
| `u3.01` | A seal in the hand | seal | Unicorn seal from Mohenjo-daro | artefact | A |
| `u4.01` | The silent signs | scroll | Indus seal with a line of signs, close up | artefact | A |
| `u4.02` | A slow ending | calendar | Abandoned Dholavira reservoir or Harappa mounds today | site photo | B |

### ih-02-vedic-age · The Vedic age

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Words, not cities | scroll | Rigveda manuscript page in Devanagari (19th c. copy) | manuscript | A |
| `u1.02` | Four books, one oldest | chips | Rigveda manuscript page; keep the four-name list as caption | manuscript | B |
| `u2.01` | Moving east | houses | Upper Ganga plain landscape or Painted Grey Ware sherd | artefact | B |
| `u2.02` | A river in dispute | scroll | Ghaggar riverbed in dry season | site photo | B |
| `u3.01` | A rajan and his assemblies | court | No period image exists; keep icon | — | C |
| `u3.02` | Later changes | houses | No period image exists; keep icon | — | C |

### ih-03-buddha-and-mahavira · Buddha and Mahavira

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u2.01` | Between two extremes | door | Fasting Buddha, Gandhara (Lahore Museum) | artefact | A |
| `u2.02` | Truths, Path and Sangha | chips | Dharmachakra relief, Sanchi gateway | site photo | A |
| `u3.01` | The ford-makers | seal | Statue of a Tirthankara, e.g. Mathura Jain image | artefact | A |
| `u3.02` | A life in Bihar | calendar | Pawapuri Jal Mandir | site photo | B |
| `u4.01` | Five vows | seal | Gommateshvara, Shravanabelagola | site photo | B |
| `u4.02` | Same region, different answers | houses | Mahabodhi Temple, Bodh Gaya | site photo | B |

### ih-04-alexander-and-magadha · Magadha and Alexander

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | A map of sixteen | houses | Punch-marked silver coin of a Mahajanapada | coin | A |
| `u1.02` | Who wrote the list? | scroll | Pali palm-leaf manuscript (Anguttara Nikaya) | manuscript | B |
| `u2.01` | From Rajagriha to Pataliputra | houses | Cyclopean wall of Rajgir | site photo | A |
| `u2.02` | Three dynasties | chips | Rajgir hills (Gridhrakuta); keep chips as caption | site photo | C |
| `u3.01` | A king from Macedonia | embassy | Alexander Mosaic, Pompeii (detail) | artefact | A |

### ih-05-mauryas · The Mauryas

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.02` | Five hundred elephants | embassy | Coin of Seleucus I with elephants | coin | A |
| `u1.03` | A Greek at court | scroll | No image of Megasthenes; keep icon | — | C |
| `u2.01` | The adviser of tradition | court | Later depiction only; prefer Pataliputra pillared-hall remains (Kumhrar) | site photo | B |
| `u2.02` | A manual for running a state | scroll | Shamasastry 1909 Arthashastra manuscript/first edition page | manuscript | A |
| `u2.03` | What is still debated | seal | Keep icon | — | C |
| `u3.01` | Son and grandson | chips | Didarganj Yakshi (Maurya-era sculpture) | artefact | B |
| `u3.03` | Remorse in stone | seal | Dhauli rock edict with elephant | site photo | A |
| `u4.01` | The code breaker | scroll | Brahmi inscription on an Ashokan pillar, close up | artefact | A |
| `u4.02` | A king with another name | seal | Maski edict naming Ashoka, or Girnar edict rock | site photo | A |
| `u5.01` | Four lions at Sarnath | seal | Lion Capital of Ashoka, Sarnath Museum | artefact | A |
| `u5.02` | Stone or legend? | chips | Keep chips | — | C |
| `u5.03` | The last Maurya | court | Bharhut stupa railing (Shunga period) | artefact | B |

### ih-06-after-the-mauryas · After the Mauryas

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Rule from Peshawar | court | Kanishka gold coin, or headless Kanishka statue, Mathura | coin | A |
| `u1.02` | Two schools of stone | seal | Gandhara Buddha beside a Mathura Buddha | artefact | A |
| `u2.01` | Two sealed rooms | door | Begram ivory plaque (Guimet / Kabul Museum) | artefact | A |
| `u2.02` | How old? | calendar | Begram painted glass goblet | artefact | B |
| `u3.01` | Lords of the Deccan | court | Satavahana coin or Karle chaitya hall | coin | A |
| `u3.02` | Poems of the Tamil lands | chips | Tamil palm-leaf manuscript | manuscript | B |

### ih-07-guptas · The Guptas

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | King of kings | court | Chandragupta I–Kumaradevi gold coin | coin | A |
| `u1.02` | Father, son, grandson | chips | Samudragupta lyre-player gold coin | coin | A |
| `u2.01` | Words added to an old pillar | seal | Allahabad pillar with Gupta inscription | artefact | A |
| `u2.02` | Kamarupa on the frontier | scroll | Allahabad pillar inscription text detail | artefact | B |
| `u3.01` | A monk walks in | embassy | Faxian, late Chinese woodcut (label as later depiction) | later depiction | B |
| `u3.02` | Three plays | chips | Raja Ravi Varma Shakuntala painting (1870s, label as later art) | painting | B |
| `u4.01` | Riders from the north-west | embassy | Alchon Hun coin of Toramana or Mihirakula | coin | A |
| `u4.02` | A slow fade | calendar | Udayagiri caves, Vidisha | site photo | C |

### ih-08-harsha · Harsha and Xuanzang

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | A family at Thanesar | court | Harsha copper plate (Banskhera) inscription | document | A |
| `u2.01` | A poet at court | scroll | Harshacharita manuscript page | manuscript | B |
| `u2.02` | Stopped at the Narmada | seal | Aihole inscription of Pulakeshin II | artefact | A |
| `u3.01` | One man, many spellings | chips | Xuanzang, 9th c. Dunhuang painting (label as later depiction) | painting | A |
| `u3.02` | A visit to Kamarupa | embassy | Nidhanpur copper plate of Bhaskaravarman, or library Xuanzang sheet (generated, label it) | document | B |

### ih-09-south-and-kashmir · Cholas, Deccan and Kashmir

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.02` | Rivals to the north | court | Virupaksha temple, Pattadakal (Chalukya) | site photo | B |
| `u2.01` | The temple at Thanjavur | houses | Brihadisvara temple, Thanjavur | site photo | A |
| `u2.02` | A fleet to Southeast Asia | embassy | Chola bronze Nataraja | artefact | B |
| `u3.01` | A history of kings | scroll | Sharada-script manuscript of Rajatarangini | manuscript | A |
| `u3.02` | The world conqueror? | seal | Martand Sun Temple ruins, Kashmir | site photo | A |

### ih-10-learning-and-art · Knowledge and stone

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | A surgeon's name | scroll | Sushruta Samhita palm-leaf manuscript | manuscript | A |
| `u1.02` | Books with many hands | chips | Charaka Samhita manuscript page | manuscript | B |
| `u2.01` | The man from Kusumapura | calendar | Aryabhata statue at IUCAA Pune (modern, label it) | later depiction | B |
| `u2.02` | The zero question | scroll | Bakhshali manuscript zero dot | manuscript | A |
| `u3.01` | A monastery in Bihar | houses | Nalanda Mahavihara ruins | site photo | A |
| `u3.02` | The end, and its limits | calendar | Nalanda burnt brick layers / ruins wide view | site photo | C |
| `u4.02` | Khajuraho | houses | Kandariya Mahadeva temple, Khajuraho | site photo | A |

### ih-11-delhi-sultanate · The Delhi Sultanate

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | From slave to sultan | court | Quwwat-ul-Islam mosque arches, Qutb complex | site photo | A |
| `u1.02` | A memory line | calendar | Coins of the five dynasties (tanka) montage | coin | B |
| `u2.01` | Finishing the Minar | houses | Qutb Minar | site photo | A |
| `u2.02` | A woman on the throne | court | Razia coin with her name | coin | A |
| `u3.01` | Fixed prices | houses | Siri Fort walls, Delhi | site photo | B |
| `u4.01` | A march that failed | embassy | Kanai Barasi rock inscription, North Guwahati | artefact | A |
| `u4.02` | Timur at Delhi | calendar | Timur at Delhi, Zafarnama miniature (later depiction) | painting | B |

### ih-12-vijayanagara-and-deccan · Vijayanagara and the Deccan

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.02` | The peak | court | Vitthala temple stone chariot, Hampi | site photo | A |
| `u2.01` | Rival to the north | houses | Bidar Fort / Mahmud Gawan madrasa | site photo | B |
| `u3.01` | A dome that whispers | door | Gol Gumbaz, Bijapur | site photo | A |
| `u3.02` | Four minarets | chips | Charminar, Hyderabad | site photo | A |

### ih-13-bhakti-and-sufi · Bhakti, Sufis and Sikh Gurus

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Hymns in Tamil | scroll | Bronze of an Alvar saint (Nammalvar) | artefact | B |
| `u1.02` | Everyday languages | chips | Kirtan-ghosha manuscript page or namghar | manuscript | B |
| `u2.01` | Beyond ritual | door | Kabir at his loom, 19th c. painting (later depiction) | painting | B |
| `u2.02` | Hindi and Assamese | scroll | Ramcharitmanas manuscript page | manuscript | A |
| `u3.01` | Shrines of the Chishtis | houses | Ajmer Sharif dargah | site photo | A |

### ih-14-babur-and-sher-shah · Babur and Sher Shah

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Twelve thousand against many more | embassy | Battle of Panipat, Baburnama miniature | painting | A |
| `u1.02` | Guns behind the wagons | court | Baburnama miniature showing guns and carts | painting | A |
| `u2.01` | One more battle | embassy | Battle of Khanwa, Baburnama miniature | painting | A |
| `u3.01` | Road with rest-houses | houses | Kos minar on the Grand Trunk Road | site photo | A |
| `u3.02` | The silver rupiya | seal | Sher Shah silver rupiya | coin | A |
| `u4.01` | Weak heirs | calendar | Purana Qila, Delhi | site photo | B |
| `u4.02` | A boy king | chips | Akbar as a boy, Akbarnama miniature | painting | B |

### ih-15-akbar · Akbar

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | The second Panipat | embassy | Second Battle of Panipat, Akbarnama miniature | painting | A |
| `u1.02` | An arrow turns a battle | chips | Hemu captured, Akbarnama miniature | painting | A |
| `u2.01` | A number for every officer | court | Akbar holding court, Akbarnama miniature | painting | A |
| `u2.02` | The tax removed | houses | Fatehpur Sikri, Buland Darwaza | site photo | B |
| `u3.01` | A creed of the court | seal | Ibadat Khana debate, Akbarnama miniature | painting | A |
| `u3.02` | The emperor's historian | scroll | Abul Fazl presenting the Akbarnama, miniature | painting | A |
| `u4.01` | A self-styled envoy | embassy | No portrait; keep icon | — | C |
| `u4.02` | Three names to separate | court | Thomas Roe portrait (period) | painting | B |

### ih-16-jahangir-to-aurangzeb · Jahangir to Aurangzeb

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | An envoy from a king | embassy | Sir Thomas Roe at Jahangir’s court, later painting | painting | A |
| `u1.02` | A small win | houses | 17th c. Surat factory engraving | painting | B |
| `u2.01` | A tomb on the Yamuna | houses | Taj Mahal | site photo | A |
| `u2.02` | Four sons, one throne | chips | Shah Jahan with his sons, Padshahnama miniature | painting | A |
| `u3.01` | The widest empire | scroll | Aurangzeb portrait miniature | painting | A |
| `u3.02` | The war in Assam | embassy | Library scene of Saraighat (generated, label it) or Lachit statue | later depiction | B |

### ih-17-marathas-and-mysore · Marathas and Mysore

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Crowned at Raigad | chips | Shivaji, 17th c. portrait (British Museum) | painting | A |
| `u1.02` | Agra and after | door | Raigad Fort | site photo | B |
| `u2.01` | January 1761 | embassy | Third Battle of Panipat, 18th c. painting | painting | A |
| `u2.02` | A decisive defeat | calendar | Panipat battlefield memorial (Kala Amb) | site photo | C |
| `u3.01` | Father and son | court | Tipu Sultan portrait, period painting | painting | A |
| `u3.02` | Tiger or lion? | seal | Tipu’s Tiger automaton (V&A) | artefact | A |

### ih-18-europeans-and-plassey · Plassey and Buxar

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Round the Cape | embassy | Vasco da Gama portrait (c.1525) or his ship | painting | A |
| `u1.02` | Calicut, 1498 | calendar | Calicut harbour, 1572 Braun & Hogenberg view | painting | A |
| `u2.01` | A Nawab and a Company | court | Siraj ud-Daulah portrait miniature | painting | A |
| `u3.01` | Three against one | embassy | Shah Alam II conveying the Diwani to Clive, Benjamin West | painting | A |
| `u3.02` | The right to collect | scroll | Treaty of Allahabad scene (same painting, detail) | painting | B |
| `u4.01` | A Nawab in name | court | Clive meeting Mir Jafar after Plassey, Francis Hayman | painting | A |
| `u4.02` | Mughal title, Company power | chips | Keep chips | — | C |

### ih-19-governors-general · The Governors-General

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | One office, three names | chips | Warren Hastings portrait, Tilly Kettle | painting | A |
| `u1.02` | The trap | seal | Lord William Bentinck portrait | painting | B |
| `u2.01` | Revenue fixed for ever | scroll | Lord Cornwallis portrait | painting | B |
| `u2.02` | Regulation XVII | seal | Regulation XVII text page, 1829 | document | A |
| `u3.01` | A Minute that changed schools | scroll | Macaulay portrait; Minute page | painting | A |
| `u3.02` | Not a Governor-General | court | Keep icon | — | C |
| `u4.01` | No male heir, no state | seal | Lord Dalhousie portrait | painting | A |
| `u4.02` | Awadh is different | door | Wajid Ali Shah portrait | painting | A |

### ih-20-reformers · Reformers

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | The Brahmo Samaj | houses | Ram Mohan Roy portrait, Rembrandt Peale 1833 | painting | A |
| `u1.02` | A law for widows | scroll | Ishwar Chandra Vidyasagar photograph | period photo | A |
| `u2.01` | A return to the Vedas | scroll | Dayananda Saraswati photograph | period photo | A |
| `u2.02` | Schools and reform | chips | Keep chips | — | C |
| `u3.01` | A student from Calcutta | door | Vivekananda, Chicago 1893 photograph | period photo | A |
| `u3.02` | A voice in Chicago | embassy | Parliament of World’s Religions 1893 platform photo | period photo | A |

### ih-21-revolt-of-1857 · The Revolt of 1857

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | The cartridge rumour | seal | Pattern 1853 Enfield rifle and paper cartridge | artefact | A |
| `u1.02` | Older anger | court | Keep icon | — | C |
| `u2.02` | An old emperor | court | Bahadur Shah Zafar, 1858 photograph | period photo | A |
| `u3.02` | The end, and Assam | door | Maniram Dewan (Assam) image or Gwalior Fort | period photo | B |
| `u4.01` | Crown for Company | chips | Queen Victoria’s 1858 Proclamation, printed sheet | document | A |
| `u4.02` | What to call it | scroll | Felice Beato photo of Secundra Bagh, Lucknow 1858 | period photo | B |

### ih-22-indigo-and-education · Indigo, press and schools

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Food or indigo | houses | Indigo vats / indigo cakes, 19th c. Bengal | period photo | A |
| `u1.02` | Nadia rises | door | Indigo factory engraving, Bengal | painting | B |
| `u1.03` | Other risings | door | Santhal rebellion, Illustrated London News 1856 | painting | A |
| `u2.01` | A mirror of indigo | scroll | Nil Darpan 1860 title page | document | A |
| `u2.02` | The publisher pays | court | Keep icon | — | C |
| `u3.01` | Wood's Despatch | scroll | Charles Wood portrait | painting | B |
| `u3.02` | Four in a row | chips | Keep chips | — | C |

### ih-23-early-congress · The early Congress

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Seventy-two delegates | court | First Congress session, Bombay 1885, group photo | period photo | A |
| `u1.02` | Who did what | seal | A. O. Hume photograph | period photo | A |
| `u2.01` | Reform, not revolt | court | Congress delegates photograph, 1890s | period photo | B |
| `u2.02` | A mentor | door | Gokhale photograph | period photo | A |
| `u3.01` | Wealth leaving India | scroll | Dadabhai Naoroji photograph; Poverty and Un-British Rule title page | period photo | A |
| `u3.02` | An MP in London | embassy | Naoroji as MP, 1892 cartoon/photo | period photo | B |
| `u4.01` | A new word | seal | Keep icon | — | C |
| `u4.02` | Pressure inside | chips | Keep chips | — | C |

### ih-24-swadeshi-and-home-rule · Swadeshi to Lucknow

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Curzon's line | seal | Lord Curzon photograph; 1905 Bengal partition map | period photo | A |
| `u1.02` | Own goods only | calendar | Swadeshi bonfire, 1905 newspaper image | period photo | B |
| `u2.01` | Three radicals | chips | Lal-Bal-Pal photographs | period photo | A |
| `u2.02` | A slogan and a theory | seal | Tilak photograph | period photo | A |
| `u3.01` | Dacca, 1906 | court | Founding of the Muslim League, Dacca 1906 photograph | period photo | A |
| `u3.02` | Haridwar, 1915 | houses | Madan Mohan Malaviya photograph | period photo | B |
| `u4.01` | Home Rule | scroll | Annie Besant photograph | period photo | A |
| `u4.02` | Lucknow, 1916 | seal | Lucknow 1916 session photograph | period photo | B |

### ih-25-year-1919 · The year 1919

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | The war ended, the powers stayed | court | Keep icon | — | C |
| `u1.02` | Prison without a trial | door | Rowlatt Act protest handbill or newspaper | document | B |
| `u1.03` | A nation stops work | calendar | Hartal crowd photograph, 1919 | period photo | B |
| `u2.02` | A walled garden | door | Jallianwala Bagh narrow entrance, 1919 photograph | period photo | A |
| `u2.03` | Counting the dead | chips | Bullet-marked wall at Jallianwala Bagh | site photo | A |
| `u3.01` | A letter from Calcutta | scroll | Tagore photograph, c.1919 | period photo | A |
| `u3.02` | The Hunter Committee | court | Keep icon | — | C |
| `u3.03` | London, 1940 | calendar | Udham Singh photograph | period photo | B |
| `u4.01` | Two kinds of rule | houses | Montagu and Chelmsford photograph | period photo | B |
| `u4.02` | Reserved or transferred? | chips | Keep chips | — | C |
| `u4.03` | Not in 1919 | calendar | Keep icon | — | C |

### ih-26-gandhi-and-noncooperation · Gandhi and Non-Cooperation

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Twenty-one years away | embassy | Gandhi as a barrister in South Africa, 1906 | period photo | A |
| `u1.02` | Home in 1915 | scroll | Gandhi on his return, 1915 photograph | period photo | A |
| `u2.01` | Indigo again | houses | Champaran indigo farm / Gandhi in Champaran 1917 | period photo | A |
| `u2.02` | I will not leave | door | Gandhi with Champaran workers | period photo | B |
| `u3.01` | Leave what the Raj offers | seal | Burning foreign cloth, 1921 photo | period photo | A |
| `u3.02` | Chauri Chaura | door | Chauri Chaura memorial | site photo | B |
| `u4.01` | Into the councils | chips | C. R. Das and Motilal Nehru photographs | period photo | A |
| `u4.02` | Obstruct from within | houses | Central Legislative Assembly, Delhi, 1920s | period photo | C |

### ih-27-simon-and-revolutionaries · Simon and the revolutionaries

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | No Indians at the table | court | Simon Go Back protest photograph, 1928 | period photo | A |
| `u1.02` | Blows at Lahore | door | Lala Lajpat Rai photograph | period photo | A |
| `u2.01` | Lahore, December 1928 | door | Bhagat Singh 1929 photograph | period photo | A |
| `u2.02` | Bombs meant to be heard | chips | Central Legislative Assembly hall photograph | period photo | B |
| `u3.01` | A poet's party | scroll | Kazi Nazrul Islam photograph | period photo | B |
| `u3.03` | Complete independence | calendar | Lahore 1929 session photograph | period photo | B |

### ih-28-salt-march · The Salt March

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | A pledge at Lahore | calendar | Nehru hoisting the flag at Lahore, 1929 | period photo | B |
| `u1.02` | A tax on everyone | seal | Salt pans of the Gujarat coast | site photo | B |
| `u1.03` | A letter before the march | scroll | Gandhi’s letter to Irwin, 1930 page | document | A |
| `u2.03` | A handful of salt | seal | Gandhi picking up salt at Dandi, 6 April 1930 | period photo | A |
| `u3.01` | South and north-west | embassy | Rajagopalachari at Vedaranyam, 1930 | period photo | B |
| `u3.02` | Dharasana | door | Dharasana satyagraha photograph | period photo | A |
| `u3.03` | The world reads | scroll | Webb Miller dispatch, newspaper front page | document | B |
| `u4.01` | Talks without the Congress | houses | First Round Table Conference photograph | period photo | A |
| `u4.02` | The Gandhi-Irwin Pact | embassy | Gandhi and Irwin, 1931 photograph | period photo | A |
| `u4.03` | Three Tables, one Congress visit | chips | Gandhi in London, 1931 photograph | period photo | A |

### ih-29-quit-india · Quit India

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | A mission from London | embassy | Stafford Cripps in India, 1942 photograph | period photo | A |
| `u1.02` | A cheque nobody wanted | seal | Keep icon | — | C |
| `u2.01` | Gowalia Tank | door | August Kranti Maidan (Gowalia Tank), Bombay | site photo | A |
| `u2.02` | Leaders vanish overnight | calendar | Aruna Asaf Ali photograph | period photo | A |
| `u3.01` | Rails and post offices | door | Quit India protest photograph, 1942 | period photo | A |
| `u4.01` | A fort in Maharashtra | scroll | Ahmednagar Fort | site photo | A |
| `u4.02` | Three mass movements | chips | Keep chips | — | C |

### ih-30-bose-and-ina · Bose and the INA

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | President twice | court | Subhas Chandra Bose at Haripura, 1938 | period photo | A |
| `u1.02` | A new bloc | seal | Forward Bloc poster/flag, 1939 | document | B |
| `u2.01` | Out of Calcutta | embassy | Bose’s Wanderer car, Netaji Bhawan | artefact | B |
| `u2.02` | Singapore, 1943 | chips | Bose reviewing the INA, Singapore 1943 | period photo | A |
| `u3.02` | Trials that backfired | court | Red Fort INA trials, 1945 photograph | period photo | A |

### ih-31-road-to-1947 · The road to 1947

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | An enlarged council | court | Lord Wavell photograph | period photo | B |
| `u2.01` | HMIS Talwar | door | HMIS Talwar / RIN mutiny photograph | period photo | A |
| `u2.02` | Twenty-two ships | embassy | Bombay harbour warships, 1946 | period photo | B |
| `u3.01` | Groups of provinces | scroll | Cabinet Mission members, 1946 photograph | period photo | A |
| `u3.02` | Calcutta, August 1946 | chips | Calcutta 1946 street photograph (use with care) | period photo | B |
| `u4.01` | Two dominions | seal | Mountbatten announcing the plan, 3 June 1947 | period photo | A |
| `u4.02` | Midnight | calendar | Nehru’s Tryst with Destiny, 15 August 1947 photograph | period photo | A |

### ih-32-building-the-republic · Building the nation

| Card | Title | Now | Proposed image | Kind | Pri |
|---|---|---|---|---|---|
| `u1.01` | Fifteen ministers | court | First cabinet of independent India photograph | period photo | A |
| `u1.02` | Birla House | calendar | Gandhi Smriti, Birla House | site photo | A |
| `u2.01` | 565 states | houses | Patel with princes, 1948 photograph | period photo | A |
| `u2.02` | Force and honours | seal | Statue of Unity / Patel photograph | period photo | B |
| `u3.01` | From charkha to chakra | seal | Flag hoisted 15 August 1947 photograph | period photo | A |
| `u3.02` | Twenty-four spokes | calendar | Ashoka Chakra close up | artefact | B |
| `u4.01` | Which Operation Vijay? | embassy | Goa liberation 1961 photograph | period photo | B |
| `u4.02` | A line of dates | chips | Keep chips | — | C |

## Lesson covers

Replace the eight shared era tiles with one image per lesson, chosen from that lesson's A list (for example the Lion Capital for `ih-05`, Qutb Minar for `ih-11`, Dandi for `ih-28`).

## Work plan

1. **Collect A images (~1 day):** download from Commons into a scratch folder, check licence, crop to 16:9 at 1080 px and convert to WebP. Record provenance as you go.
2. **Wire them in:** add `img`, `imageCaption` (English and Assamese, pending review), `imageLayout: "wide"` and `imageKind` to each card. Keep `art` only where no image is added.
3. **Covers:** set each lesson `portrait` and the course `face` to its new image.
4. **B images:** second pass, same process.
5. **Check:** `scripts/verify.sh`, then play two lessons in English and Assamese at phone width to confirm captions, credits and loading.
6. **Publish:** commit, push, `scripts/deploy_cloudflare.sh`.
