# Indian History lesson images: integrated register

Integrated 2026-11-07 from the drafts in `output/imagegen/indian-history/` (ledger: `indian-history-generation-queue.json`). **197 story cards** now show a picture: **189 AI-generated illustrations** and **8 licensed photographs**. 32 lessons also have their own cover (`content/media/<lesson>/cover.webp`, reused from a card image in that lesson). `ih-33` keeps its era tile.

Every generated image shows the credit "AI illustration · not historical evidence" on the card. Photographs show their photographer and licence and use a caption. Historical fidelity and Assamese review remain pending, as recorded in the ledger.

Sizes: generated images are 1080 × 608 WebP (quality 80) as full-width hero pictures. Photographs keep their shape, at most 1080 px on the long side, and use the `contain` caption layout. `build.py` makes the `@480` copies.

Not used: `ih-28.u2.03` (Dandi photo only 234 × 328 px) and `ih-30.u1.02` (modern flag vector, not verified as the 1939 design). These cards keep their icons.

## Licensed photographs

| Card | File | Credit | Licence | Source |
|---|---|---|---|---|
| `ih-01-indus-cities.u1.02` | `content/media/ih-01-indus-cities/u1.02.webp` | Photo: Gary Todd, CC0 1.0, via Wikimedia Commons. Resized for WebP preview; original preserved. | CC0 1.0 | https://commons.wikimedia.org/wiki/File:Dancing_girl_of_Mohenjo-daro.jpg |
| `ih-05-mauryas.u3.01` | `content/media/ih-05-mauryas/u3.01.webp` | Photo: Abhishek Paliwal, CC BY 3.0, via Wikimedia Commons. Resized for WebP preview; original preserved. | CC BY 3.0 | https://commons.wikimedia.org/wiki/File:Didarganj_Yakshi.webp |
| `ih-26-gandhi-and-noncooperation.u1.01` | `content/media/ih-26-gandhi-and-noncooperation/u1.01.webp` | Photograph: unknown author; public domain, via Wikimedia Commons. | Public domain | https://commons.wikimedia.org/wiki/File:Gandhi_London_1906.jpg |
| `ih-26-gandhi-and-noncooperation.u1.02` | `content/media/ih-26-gandhi-and-noncooperation/u1.02.webp` | Photograph: unknown author; public domain, via Wikimedia Commons. | Public domain | https://commons.wikimedia.org/wiki/File:Mahatma_and_Kasturba_Gandhi_on_their_return_to_India_from_South_Africa_in_1915.jpg |
| `ih-26-gandhi-and-noncooperation.u2.02` | `content/media/ih-26-gandhi-and-noncooperation/u2.02.webp` | Photo: Khanazmat, CC BY-SA 4.0, via Wikimedia Commons. Resized WebP derivative; original preserved. | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:StonePillar_GandhiMuseum.jpg |
| `ih-28-salt-march.u1.03` | `content/media/ih-28-salt-march/u1.03.webp` | Photograph: unknown author; public domain, via Wikimedia Commons. | Public domain | https://commons.wikimedia.org/wiki/File:Gandhi_writing,_1940.jpg |
| `ih-28-salt-march.u4.03` | `content/media/ih-28-salt-march/u4.03.webp` | Photograph: unknown author; public domain, via Wikimedia Commons. | Public domain | https://commons.wikimedia.org/wiki/File:Gandhi_leaving_his_Knightsbridge_office_in_London.jpg |
| `ih-32-building-the-republic.u3.02` | `content/media/ih-32-building-the-republic/u3.02.webp` | Original: Government of India; vector: MapGrid; public domain, via Wikimedia Commons. | Public domain | https://commons.wikimedia.org/wiki/File:Ashoka_Chakra.svg |

## Generated illustrations

| Card | File | Research sources |
|---|---|---|
| `ih-01-indus-cities.u2.01` | `content/media/ih-01-indus-cities/u2.01.webp` | https://www.harappa.com/blog/mohenjo-daro-street-drains |
| `ih-01-indus-cities.u2.02` | `content/media/ih-01-indus-cities/u2.02.webp` | https://www.harappa.com/content/great-bath-mohenjo-daro-c |
| `ih-01-indus-cities.u3.01` | `content/media/ih-01-indus-cities/u3.01.webp` | https://www.harappa.com/sites/default/files/pdf/Rediscovering_Harappa.pdf |
| `ih-01-indus-cities.u4.01` | `content/media/ih-01-indus-cities/u4.01.webp` | https://www.harappa.com/slide/unicorn-seal-1 |
| `ih-01-indus-cities.u4.02` | `content/media/ih-01-indus-cities/u4.02.webp` | https://whc.unesco.org/en/list/1645/ |
| `ih-02-vedic-age.u1.01` | `content/media/ih-02-vedic-age/u1.01.webp` | https://www.unesco.org/en/memory-world/rigveda |
| `ih-02-vedic-age.u1.02` | `content/media/ih-02-vedic-age/u1.02.webp` | https://www.unesco.org/en/memory-world/rigveda |
| `ih-02-vedic-age.u2.01` | `content/media/ih-02-vedic-age/u2.01.webp` | https://www.unesco.org/en/memory-world/rigveda |
| `ih-02-vedic-age.u2.02` | `content/media/ih-02-vedic-age/u2.02.webp` | https://censusindia.gov.in/nada/index.php/catalog/440/download/1408/DH_2011_0611_PART_A_DCHB_SIRSA.pdf |
| `ih-03-buddha-and-mahavira.u2.01` | `content/media/ih-03-buddha-and-mahavira/u2.01.webp` | https://lahoremuseum.punjab.gov.pk/, https://doam.gov.pk/public/heritage-sites/788 |
| `ih-03-buddha-and-mahavira.u2.02` | `content/media/ih-03-buddha-and-mahavira/u2.02.webp` | https://whc.unesco.org/en/list/524 |
| `ih-03-buddha-and-mahavira.u3.01` | `content/media/ih-03-buddha-and-mahavira/u3.01.webp` | https://www.clevelandart.org/print/art/1962.47, https://www.metmuseum.org/fr/essays/jain-sculpture |
| `ih-03-buddha-and-mahavira.u3.02` | `content/media/ih-03-buddha-and-mahavira/u3.02.webp` | https://tourism.bihar.gov.in/en/destinations/nalanda/jal-mandir-pawapuri, https://nalanda.nic.in/en/tourist-place/pawapuri-jal-mandir/ |
| `ih-03-buddha-and-mahavira.u4.01` | `content/media/ih-03-buddha-and-mahavira/u4.01.webp` | https://karnatakatourism.org/en/attractions/shravanabelagola/ |
| `ih-03-buddha-and-mahavira.u4.02` | `content/media/ih-03-buddha-and-mahavira/u4.02.webp` | https://whc.unesco.org/en/list/1056 |
| `ih-04-alexander-and-magadha.u1.01` | `content/media/ih-04-alexander-and-magadha/u1.01.webp` | https://www.britishmuseum.org/collection/object/C_1869-1203-48, https://www.clevelandart.org/art/1967.242 |
| `ih-04-alexander-and-magadha.u1.02` | `content/media/ih-04-alexander-and-magadha/u1.02.webp` | https://www.digitalcollections.manchester.ac.uk/collections/pali, https://omeka.qub.ac.uk/exhibits/show/irelandandcolonies/palmleaf |
| `ih-04-alexander-and-magadha.u2.01` | `content/media/ih-04-alexander-and-magadha/u2.01.webp` | https://nalanda.nic.in/en/tourist-place/cyclopean-wall/ |
| `ih-04-alexander-and-magadha.u3.01` | `content/media/ih-04-alexander-and-magadha/u3.01.webp` | https://www.museoarcheologiconapoli.it/en/the-restoration-of-the-mosaic-of-alexander/ |
| `ih-05-mauryas.u1.02` | `content/media/ih-05-mauryas/u1.02.webp` | https://www.colorado.edu/project/expressionsofidentity/silver-tetradrachm-seleucia-ii-second-workshop-2965-bce-seleucus-i |
| `ih-05-mauryas.u2.01` | `content/media/ih-05-mauryas/u2.01.webp` | https://patna.nic.in/tourist-place/kumhrar-park/ |
| `ih-05-mauryas.u2.02` | `content/media/ih-05-mauryas/u2.02.webp` | https://openlibrary.org/books/OL58247957M/The_Artha%C5%9B%C4%81stra |
| `ih-05-mauryas.u3.03` | `content/media/ih-05-mauryas/u3.03.webp` | https://nma.gov.in/showfile.php?lang=1&level=2&lid=1286&ls_id=1022&nma_type=0, https://ignca.gov.in/Asi_data/41424.pdf |
| `ih-05-mauryas.u4.01` | `content/media/ih-05-mauryas/u4.01.webp` | https://nationalmuseumindia.gov.in/en/collections/index/21 |
| `ih-05-mauryas.u4.02` | `content/media/ih-05-mauryas/u4.02.webp` | https://raichur.nic.in/en/tourist-place/asoka-inscription/ |
| `ih-05-mauryas.u5.01` | `content/media/ih-05-mauryas/u5.01.webp` | https://www.sarnathmuseumasi.org/gallery/Gallery3-Acc-No-355.html, https://asisarnathcircle.in/lion-capital.php |
| `ih-05-mauryas.u5.03` | `content/media/ih-05-mauryas/u5.03.webp` | https://museumsofindia.gov.in/repository/record/im_kol-Bharhut-Gateway-10360 |
| `ih-06-after-the-mauryas.u1.01` | `content/media/ih-06-after-the-mauryas/u1.01.webp` | https://museumsofindia.gov.in/repository/record/alh_ald-AM-GC-100-7666, https://www.britishmuseum.org/collection/object/C_1989-0904-4013 |
| `ih-06-after-the-mauryas.u1.02` | `content/media/ih-06-after-the-mauryas/u1.02.webp` | https://www.ashmolean.org/standing-figure-buddha, https://www.metmuseum.org/art/collection/search/38198 |
| `ih-06-after-the-mauryas.u2.01` | `content/media/ih-06-after-the-mauryas/u2.01.webp` | https://www.guimet.fr/fr/nos-collections/afghanistan-pakistan/deux-figures-feminines-sous-un-portique-tresor-de-begram, https://ignca.gov.in/Asi_data/62722.pdf |
| `ih-06-after-the-mauryas.u2.02` | `content/media/ih-06-after-the-mauryas/u2.02.webp` | https://ignca.gov.in/Asi_data/62722.pdf |
| `ih-06-after-the-mauryas.u3.01` | `content/media/ih-06-after-the-mauryas/u3.01.webp` | https://maharashtratourism.gov.in/wp-content/uploads/2024/07/MH-Leaflet-Buddhist-Heritage-Circuit-Slides.pdf |
| `ih-06-after-the-mauryas.u3.02` | `content/media/ih-06-after-the-mauryas/u3.02.webp` | https://www.csmc.uni-hamburg.de/hamburgs-schriftschaetze/english/the-glory-of-vishnu.html, https://tnarch.gov.in/goml/stock |
| `ih-07-guptas.u1.01` | `content/media/ih-07-guptas/u1.01.webp` | https://www.museumsofindia.gov.in/repository/record/alh_ald-AM-GC-10-7669, https://artsandculture.google.com/asset/coin-of-chandragupta/zAHnDFySvL6U5A |
| `ih-07-guptas.u1.02` | `content/media/ih-07-guptas/u1.02.webp` | https://networksofthepast.csmvs.in/object/king-samudraguta-playing-the-lyre/, https://ignca.gov.in/Asi_data/47214.pdf |
| `ih-07-guptas.u2.01` | `content/media/ih-07-guptas/u2.01.webp` | https://siddham.network/object/ob00001/, https://prayagraj.nic.in/top-attractions/ |
| `ih-07-guptas.u2.02` | `content/media/ih-07-guptas/u2.02.webp` | https://siddham.network/object/ob00001/ |
| `ih-07-guptas.u3.01` | `content/media/ih-07-guptas/u3.01.webp` | https://www.gutenberg.org/cache/epub/2124/pg2124-images.html |
| `ih-07-guptas.u3.02` | `content/media/ih-07-guptas/u3.02.webp` | https://www.rajaravivarmaartgallery.kerala.gov.in/index.php/gallery-1-3, https://artsandculture.google.com/asset/shakuntala-s-impending-calamity-raja-ravi-varma/zQFyRiLZH8Se6Q |
| `ih-07-guptas.u4.01` | `content/media/ih-07-guptas/u4.01.webp` | https://depts.washington.edu/silkroad/exhibit/hephthalites/i_heph_113_o.html |
| `ih-07-guptas.u4.02` | `content/media/ih-07-guptas/u4.02.webp` | https://vidisha.nic.in/en/tourist-place/udaigiri-cave/ |
| `ih-08-harsha.u1.01` | `content/media/ih-08-harsha/u1.01.webp` | https://www.indoskript.phil.uni-wuerzburg.de/manuscripts/details/544 |
| `ih-08-harsha.u2.01` | `content/media/ih-08-harsha/u2.01.webp` | https://archive.org/details/harsacaritaofban00banaiala |
| `ih-08-harsha.u2.02` | `content/media/ih-08-harsha/u2.02.webp` | https://bagalkot.nic.in/en/tourist-place/aihole/ |
| `ih-08-harsha.u3.01` | `content/media/ih-08-harsha/u3.01.webp` | https://www.metmuseum.org/art/collection/search/45372, https://jpsearch.go.jp/en/item/cobas-158924 |
| `ih-08-harsha.u3.02` | `content/media/ih-08-harsha/u3.02.webp` |  |
| `ih-09-south-and-kashmir.u1.02` | `content/media/ih-09-south-and-kashmir/u1.02.webp` | https://whc.unesco.org/en/list/239, https://ignca.gov.in/Asi_data/36615.pdf |
| `ih-09-south-and-kashmir.u2.01` | `content/media/ih-09-south-and-kashmir/u2.01.webp` | https://whc.unesco.org/en/list/250 |
| `ih-09-south-and-kashmir.u2.02` | `content/media/ih-09-south-and-kashmir/u2.02.webp` | https://www.metmuseum.org/art/collection/search/39329 |
| `ih-09-south-and-kashmir.u3.01` | `content/media/ih-09-south-and-kashmir/u3.01.webp` | https://searcharchives.bl.uk/catalog/040-003396922 |
| `ih-09-south-and-kashmir.u3.02` | `content/media/ih-09-south-and-kashmir/u3.02.webp` | https://anantnag.nic.in/tourist-place/martand-sun-temple/, https://ignca.gov.in/Asi_data/83540.pdf |
| `ih-10-learning-and-art.u1.01` | `content/media/ih-10-learning-and-art/u1.01.webp` | https://www.unesco.org/en/memory-world/susrutamhita-sahottartantra-manuscript?hub=1081 |
| `ih-10-learning-and-art.u1.02` | `content/media/ih-10-learning-and-art/u1.02.webp` | https://www.ncbi.nlm.nih.gov/nlmcatalog/351138, https://rarebooksocietyofindia.org/book_archive/196174216674_10153720923176675.pdf |
| `ih-10-learning-and-art.u2.01` | `content/media/ih-10-learning-and-art/u2.01.webp` | https://web.iucaa.in/~library/photogal/campus/mainb.htm, https://web.iucaa.in/~library/photogal/campus/CS3.jpg |
| `ih-10-learning-and-art.u2.02` | `content/media/ih-10-learning-and-art/u2.02.webp` | https://glam.web.ox.ac.uk/node/218481 |
| `ih-10-learning-and-art.u3.01` | `content/media/ih-10-learning-and-art/u3.01.webp` | https://whc.unesco.org/en/list/1502/ |
| `ih-10-learning-and-art.u3.02` | `content/media/ih-10-learning-and-art/u3.02.webp` | https://whc.unesco.org/en/list/1502/ |
| `ih-10-learning-and-art.u4.02` | `content/media/ih-10-learning-and-art/u4.02.webp` | https://whc.unesco.org/en/list/240/, https://culture.gov.in/khajuraho-group-monuments |
| `ih-11-delhi-sultanate.u1.01` | `content/media/ih-11-delhi-sultanate/u1.01.webp` | https://whc.unesco.org/en/list/233, https://ignca.gov.in/Asi_data/87960.pdf |
| `ih-11-delhi-sultanate.u1.02` | `content/media/ih-11-delhi-sultanate/u1.02.webp` | https://m.rbi.org.in/Commonman/English/Currency/Scripts/Medieval.aspx |
| `ih-11-delhi-sultanate.u2.01` | `content/media/ih-11-delhi-sultanate/u2.01.webp` | https://whc.unesco.org/en/list/233 |
| `ih-11-delhi-sultanate.u2.02` | `content/media/ih-11-delhi-sultanate/u2.02.webp` | https://sarmaya.in/objects/numismatics/jalaluddin-razia-silver-tanka/, https://artsandculture.google.com/asset/razia-sultan-silver-tanka-razia-sultan/bQEWXgHZsJcJFA |
| `ih-11-delhi-sultanate.u3.01` | `content/media/ih-11-delhi-sultanate/u3.01.webp` | https://nmma.nic.in/nmma/builtDetail.do?dynasty=11&refId=11421, https://ignca.gov.in/asi_reports/sd140ibs0001_4.pdf |
| `ih-11-delhi-sultanate.u4.01` | `content/media/ih-11-delhi-sultanate/u4.01.webp` | https://assam.mygov.in/en/talk/kanai-barasi-bowa-rock-inscription/, https://culturalaffairs.assam.gov.in/portlet-innerpage/protected-archaeological-sites-and-monuments |
| `ih-11-delhi-sultanate.u4.02` | `content/media/ih-11-delhi-sultanate/u4.02.webp` | https://www.metmuseum.org/art/collection/search/451303, https://collections.si.edu/search/detail/edanmdm%3Afsg_F1948.18?print=yes |
| `ih-12-vijayanagara-and-deccan.u1.02` | `content/media/ih-12-vijayanagara-and-deccan/u1.02.webp` | https://www.asihampicircle.in/vittala-temple-complex-and-its-surrounding/, https://vijayanagara.nic.in/en/tourist-place/stone-chariot-hampi/ |
| `ih-12-vijayanagara-and-deccan.u2.01` | `content/media/ih-12-vijayanagara-and-deccan/u2.01.webp` | https://old.karnatakatourism.org/tour-item/mohamud-gawan-madrasa-bidar/, https://www.incredibleindia.gov.in/en/karnataka/bidar/mahmud-gawan-madrasa |
| `ih-12-vijayanagara-and-deccan.u3.01` | `content/media/ih-12-vijayanagara-and-deccan/u3.01.webp` | https://vijayapura.nic.in/en/tourist-place/gol-gumbaz/ |
| `ih-12-vijayanagara-and-deccan.u3.02` | `content/media/ih-12-vijayanagara-and-deccan/u3.02.webp` | https://hyderabad.telangana.gov.in/tourist-place/charminar/ |
| `ih-13-bhakti-and-sufi.u1.01` | `content/media/ih-13-bhakti-and-sufi/u1.01.webp` | https://govtmuseumchennai.org/uploads/topics/16569321498920.pdf |
| `ih-13-bhakti-and-sufi.u1.02` | `content/media/ih-13-bhakti-and-sufi/u1.02.webp` | https://jorhat.assam.gov.in/tourist-place-detail/251 |
| `ih-13-bhakti-and-sufi.u2.01` | `content/media/ih-13-bhakti-and-sufi/u2.01.webp` | https://collections.vam.ac.uk/item/O69361/kabir-painting-unknown/ |
| `ih-13-bhakti-and-sufi.u2.02` | `content/media/ih-13-bhakti-and-sufi/u2.02.webp` | https://www.unesco.org/en/articles/indias-literary-treasures-inscribed-2024-memory-world-committee-asia-and-pacific-regional-register?hub=412 |
| `ih-13-bhakti-and-sufi.u3.01` | `content/media/ih-13-bhakti-and-sufi/u3.01.webp` | https://www.tourism.rajasthan.gov.in/the-ajmer-sharif-dargah.html |
| `ih-14-babur-and-sher-shah.u1.01` | `content/media/ih-14-babur-and-sher-shah/u1.01.webp` | https://panipat.gov.in/first-battle/ |
| `ih-14-babur-and-sher-shah.u1.02` | `content/media/ih-14-babur-and-sher-shah/u1.02.webp` | https://panipat.gov.in/first-battle/ |
| `ih-14-babur-and-sher-shah.u2.01` | `content/media/ih-14-babur-and-sher-shah/u2.01.webp` | https://ignca.gov.in/Asi_data/10571.pdf, https://asia.si.edu/explore-art-culture/collections/collections-areas/southasian-himalayan/discovering-babur/writing-my-truth-the-mughal-emperor-babur/making-the-baburnama/ |
| `ih-14-babur-and-sher-shah.u3.01` | `content/media/ih-14-babur-and-sher-shah/u3.01.webp` | https://haryanatourism.gov.in/places_of_interest/kos-minar/, https://archaeology.delhi.gov.in/tender/minor-conservation-and-development-works-kos-minar-monument-near-northern-gateway |
| `ih-14-babur-and-sher-shah.u3.02` | `content/media/ih-14-babur-and-sher-shah/u3.02.webp` | https://www.rbi.org.in/scripts/mc_mughal.aspx |
| `ih-14-babur-and-sher-shah.u4.01` | `content/media/ih-14-babur-and-sher-shah/u4.01.webp` | https://dmsoutheast.delhi.gov.in/tourist-place/purana-quila/, https://ignca.gov.in/asi_reports/sd37pq0001a.pdf |
| `ih-14-babur-and-sher-shah.u4.02` | `content/media/ih-14-babur-and-sher-shah/u4.02.webp` | https://www.philamuseum.org/objects/101282 |
| `ih-15-akbar.u1.01` | `content/media/ih-15-akbar/u1.01.webp` | https://www.ngv.vic.gov.au/essay/mughal-painting-under-akbar-the-melbourne-hamza-nama-and-akbar-nama-paintings/ |
| `ih-15-akbar.u1.02` | `content/media/ih-15-akbar/u1.02.webp` | https://www.ngv.vic.gov.au/essay/mughal-painting-under-akbar-the-melbourne-hamza-nama-and-akbar-nama-paintings/ |
| `ih-15-akbar.u2.01` | `content/media/ih-15-akbar/u2.01.webp` | https://asia.si.edu/explore-art-culture/collections/collections-areas/southasian-himalayan/discovering-babur/writing-my-truth-the-mughal-emperor-babur/making-the-baburnama/ |
| `ih-15-akbar.u2.02` | `content/media/ih-15-akbar/u2.02.webp` | https://whc.unesco.org/en/list/255/ |
| `ih-15-akbar.u3.01` | `content/media/ih-15-akbar/u3.01.webp` | https://www.icm.gov.mo/rc/viewer/20013/957 |
| `ih-15-akbar.u3.02` | `content/media/ih-15-akbar/u3.02.webp` | https://www.metmuseum.org/art/collection/search/448471?searchField=All, https://digital.libraries.psu.edu/digital/collection/arthist2/id/37900/ |
| `ih-15-akbar.u4.02` | `content/media/ih-15-akbar/u4.02.webp` | https://www.npg.org.uk/collections/search/person/mp03840/sir-thomas-roe?sText=sir&search=sas |
| `ih-16-jahangir-to-aurangzeb.u1.01` | `content/media/ih-16-jahangir-to-aurangzeb/u1.01.webp` | https://committees.parliament.uk/committee/301/speakers-advisory-committee-on-works-of-art/news/92205/ |
| `ih-16-jahangir-to-aurangzeb.u1.02` | `content/media/ih-16-jahangir-to-aurangzeb/u1.02.webp` | https://searcharchives.bl.uk/catalog/032-000173250 |
| `ih-16-jahangir-to-aurangzeb.u2.01` | `content/media/ih-16-jahangir-to-aurangzeb/u2.01.webp` | https://whc.unesco.org/en/list/252/ |
| `ih-16-jahangir-to-aurangzeb.u2.02` | `content/media/ih-16-jahangir-to-aurangzeb/u2.02.webp` | https://www.rct.uk/collection/1005025-l/shah-jahan-receives-his-three-eldest-sons-and-asaf-khan-during-his-accession |
| `ih-16-jahangir-to-aurangzeb.u3.01` | `content/media/ih-16-jahangir-to-aurangzeb/u3.01.webp` | https://collections.lacma.org/object/30112, https://www.metmuseum.org/art/collection/search/450610 |
| `ih-16-jahangir-to-aurangzeb.u3.02` | `content/media/ih-16-jahangir-to-aurangzeb/u3.02.webp` | https://jorhat.assam.gov.in/sites/default/files/public_utility/Jorhat-October%20Newsletter.pdf |
| `ih-17-marathas-and-mysore.u1.01` | `content/media/ih-17-marathas-and-mysore/u1.01.webp` | https://collections.louvre.fr/en/ark:/53355/cl010327225 |
| `ih-17-marathas-and-mysore.u1.02` | `content/media/ih-17-marathas-and-mysore/u1.02.webp` | https://raigad.gov.in/en/tourist-place/forts-in-raigad/ |
| `ih-17-marathas-and-mysore.u2.01` | `content/media/ih-17-marathas-and-mysore/u2.01.webp` | https://panipat.gov.in/third-battle/ |
| `ih-17-marathas-and-mysore.u2.02` | `content/media/ih-17-marathas-and-mysore/u2.02.webp` | https://panipat.gov.in/tourist-place/the-kala-amb-park/ |
| `ih-17-marathas-and-mysore.u3.01` | `content/media/ih-17-marathas-and-mysore/u3.01.webp` | https://www.npg.org.uk/collections/search/person/mp62177/tipu-sultan-of-mysore |
| `ih-17-marathas-and-mysore.u3.02` | `content/media/ih-17-marathas-and-mysore/u3.02.webp` | https://www.vam.ac.uk/articles/tipus-tiger |
| `ih-18-europeans-and-plassey.u1.01` | `content/media/ih-18-europeans-and-plassey/u1.01.webp` | https://www.rmg.co.uk/collections/objects/rmgc-object-106482 |
| `ih-18-europeans-and-plassey.u1.02` | `content/media/ih-18-europeans-and-plassey/u1.02.webp` | https://artsandculture.google.com/asset/views-of-kozhikode-and-kannur-kerala-with-hormuz-iran-and-elmina-ghana-0097/ZwGI8_vPDqpWUA |
| `ih-18-europeans-and-plassey.u2.01` | `content/media/ih-18-europeans-and-plassey/u2.01.webp` | https://www.nationaltrust.org.uk/visit/wales/powis-castle-and-garden/the-clive-museum-collection-at-powis-castle |
| `ih-18-europeans-and-plassey.u3.01` | `content/media/ih-18-europeans-and-plassey/u3.01.webp` | https://natlib.govt.nz/records/49329286 |
| `ih-18-europeans-and-plassey.u3.02` | `content/media/ih-18-europeans-and-plassey/u3.02.webp` | https://natlib.govt.nz/records/49329286 |
| `ih-18-europeans-and-plassey.u4.01` | `content/media/ih-18-europeans-and-plassey/u4.01.webp` | https://www.nationaltrust.org.uk/visit/wales/powis-castle-and-garden/the-clive-museum-collection-at-powis-castle |
| `ih-19-governors-general.u1.01` | `content/media/ih-19-governors-general/u1.01.webp` | https://www.npg.org.uk/collections/search/portrait-list.php?displayNo=40&sText=warren+hastings&search=sp |
| `ih-19-governors-general.u1.02` | `content/media/ih-19-governors-general/u1.02.webp` | https://ignca.gov.in/Asi_data/1808.pdf |
| `ih-19-governors-general.u2.01` | `content/media/ih-19-governors-general/u2.01.webp` | https://www.npg.org.uk/collections/search/portrait/mw01483/Charles-Cornwallis-1st-Marquess-Cornwallis |
| `ih-19-governors-general.u2.02` | `content/media/ih-19-governors-general/u2.02.webp` | https://www.indiacode.nic.in/bitstream/123456789/19146/1/a1874-15.pdf |
| `ih-19-governors-general.u3.01` | `content/media/ih-19-governors-general/u3.01.webp` | https://www.npg.org.uk/collections/search/person/mp02855/thomas-babington-macaulay-baron-macaulay?displayStyle=thumb |
| `ih-19-governors-general.u4.01` | `content/media/ih-19-governors-general/u4.01.webp` | https://ignca.gov.in/Asi_data/1808.pdf |
| `ih-19-governors-general.u4.02` | `content/media/ih-19-governors-general/u4.02.webp` | https://www.rct.uk/collection/publications/eastern-encounters/wajid-ali-shah-and-his-wives-listen-to-a-performance-by-najib-al-daula |
| `ih-20-reformers.u1.01` | `content/media/ih-20-reformers/u1.01.webp` | https://npg.si.edu/object/npg_MA240715 |
| `ih-20-reformers.u1.02` | `content/media/ih-20-reformers/u1.02.webp` | https://static.pib.gov.in/WriteReadData/userfiles/Unsung%20Heroes%20of%20Freedom%20Movement_p1.pdf |
| `ih-20-reformers.u2.01` | `content/media/ih-20-reformers/u2.01.webp` | https://postagestamps.gov.in/Pdf/2023/Dayanand%20Saraswati%20BROCHURE.pdf |
| `ih-20-reformers.u3.01` | `content/media/ih-20-reformers/u3.01.webp` | https://artsandculture.google.com/asset/swami-vivekananda-sitting-self-signed-photo/7gHEur0KvwmQFw?hl=en |
| `ih-20-reformers.u3.02` | `content/media/ih-20-reformers/u3.02.webp` | https://artsandculture.google.com/asset/swami-vivekananda-at-chicago/EAH-ARRSfSf49g?hl=en |
| `ih-21-revolt-of-1857.u1.01` | `content/media/ih-21-revolt-of-1857/u1.01.webp` | https://www.royal-irish.co.uk/artefacts/cartridges-and-indian-mutiny |
| `ih-21-revolt-of-1857.u2.02` | `content/media/ih-21-revolt-of-1857/u2.02.webp` | https://collection.nam.ac.uk/detail.php?acc=1971-12-40-4 |
| `ih-21-revolt-of-1857.u3.02` | `content/media/ih-21-revolt-of-1857/u3.02.webp` | https://gwalior.nic.in/en/tourist-place/the-fort/ |
| `ih-21-revolt-of-1857.u4.01` | `content/media/ih-21-revolt-of-1857/u4.01.webp` | https://searcharchives.bl.uk/catalog/032-002273023 |
| `ih-21-revolt-of-1857.u4.02` | `content/media/ih-21-revolt-of-1857/u4.02.webp` | https://library.brown.edu/exhibits/fashioning-insurrection/india/press-and-popular-sentiment/7-5.html |
| `ih-22-indigo-and-education.u1.01` | `content/media/ih-22-indigo-and-education/u1.01.webp` | https://searcharchives.bl.uk/catalog/032-003268472 |
| `ih-22-indigo-and-education.u1.02` | `content/media/ih-22-indigo-and-education/u1.02.webp` | https://searcharchives.bl.uk/catalog/032-003268472 |
| `ih-22-indigo-and-education.u1.03` | `content/media/ih-22-indigo-and-education/u1.03.webp` | https://en.wikisource.org/wiki/The_Aborigines%27_Friend_and_the_Colonial_Intelligencer/1855/Insurrection_of_the_Santhals |
| `ih-22-indigo-and-education.u2.01` | `content/media/ih-22-indigo-and-education/u2.01.webp` | https://openlibrary.org/books/OL7117594M/Nil_darpan_or_The_indigo_planting_mirror |
| `ih-22-indigo-and-education.u3.01` | `content/media/ih-22-indigo-and-education/u3.01.webp` | https://www.npg.org.uk/collections/search/person/mp01977/charles-wood-1st-viscount-halifax?displayStyle=thumb |
| `ih-23-early-congress.u1.01` | `content/media/ih-23-early-congress/u1.01.webp` | https://inc.in/brief-history-of-congress |
| `ih-23-early-congress.u1.02` | `content/media/ih-23-early-congress/u1.02.webp` | https://www.nhm.ac.uk/our-science/services/collections/zoology/birds/skins/hume.html |
| `ih-23-early-congress.u2.01` | `content/media/ih-23-early-congress/u2.01.webp` | https://inc.in/brief-history-of-congress |
| `ih-23-early-congress.u2.02` | `content/media/ih-23-early-congress/u2.02.webp` | https://inc.in/leadership/past-party-presidents/gopal-krishna-gokhale |
| `ih-23-early-congress.u3.01` | `content/media/ih-23-early-congress/u3.01.webp` | https://heritagecollections.parliament.uk/exhibits/pioneers/ |
| `ih-23-early-congress.u3.02` | `content/media/ih-23-early-congress/u3.02.webp` | https://heritagecollections.parliament.uk/exhibits/pioneers/ |
| `ih-24-swadeshi-and-home-rule.u1.01` | `content/media/ih-24-swadeshi-and-home-rule/u1.01.webp` | https://www.rgs.org/our-collections/stories-from-our-collections/explore-our-collections/portrait-of-george-curzon |
| `ih-24-swadeshi-and-home-rule.u1.02` | `content/media/ih-24-swadeshi-and-home-rule/u1.02.webp` | https://inc.in/brief-history-of-congress/1905-1915 |
| `ih-24-swadeshi-and-home-rule.u2.01` | `content/media/ih-24-swadeshi-and-home-rule/u2.01.webp` | https://malaviyamission.org/AboutMahamana/Intrepid-Freedom-Fighter-Detail.php?id=3 |
| `ih-24-swadeshi-and-home-rule.u2.02` | `content/media/ih-24-swadeshi-and-home-rule/u2.02.webp` | https://inc.in/brief-history-of-congress/1905-1915 |
| `ih-24-swadeshi-and-home-rule.u3.01` | `content/media/ih-24-swadeshi-and-home-rule/u3.01.webp` | https://en.banglapedia.org/index.php/Muslim_League |
| `ih-24-swadeshi-and-home-rule.u3.02` | `content/media/ih-24-swadeshi-and-home-rule/u3.02.webp` | https://www.bhu.ac.in/Images/files/main.pdf |
| `ih-24-swadeshi-and-home-rule.u4.01` | `content/media/ih-24-swadeshi-and-home-rule/u4.01.webp` | https://wellcomecollection.org/works/u7kcygnt |
| `ih-24-swadeshi-and-home-rule.u4.02` | `content/media/ih-24-swadeshi-and-home-rule/u4.02.webp` | https://inc.in/inc-sessions, https://malaviyamission.org/AboutMahamana/Intrepid-Freedom-Fighter-Detail.php?id=3 |
| `ih-25-year-1919.u1.02` | `content/media/ih-25-year-1919/u1.02.webp` | https://www.publicationsdivision.nic.in/catalog/view/theme/default/images/new_ngm_final/timeline/index2.html |
| `ih-25-year-1919.u1.03` | `content/media/ih-25-year-1919/u1.03.webp` | https://gandhismriti.gov.in/more/chronology-mahatma-gandhi |
| `ih-25-year-1919.u2.02` | `content/media/ih-25-year-1919/u2.02.webp` | https://www.incredibleindia.gov.in/en/punjab/amritsar/jallianwala-bagh |
| `ih-25-year-1919.u2.03` | `content/media/ih-25-year-1919/u2.03.webp` | https://amritsar.nic.in/tourist-place/jallian-wala-bagh/ |
| `ih-25-year-1919.u3.01` | `content/media/ih-25-year-1919/u3.01.webp` | https://npg.si.edu/Rabindranath_Tagore |
| `ih-25-year-1919.u3.03` | `content/media/ih-25-year-1919/u3.03.webp` | https://www.culture.gov.in/files/publications_documents/Martyrs_Vol_1_Part_II_06_03_2019_2.pdf |
| `ih-25-year-1919.u4.01` | `content/media/ih-25-year-1919/u4.01.webp` | https://archives.trin.cam.ac.uk/index.php/montagu-edwin-samuel-1879-1924-politician, https://www.npg.org.uk/collections/search/person/mp85256/frederic-john-napier-thesiger-1st-viscount-chelmsford |
| `ih-26-gandhi-and-noncooperation.u2.01` | `content/media/ih-26-gandhi-and-noncooperation/u2.01.webp` | https://www.gandhiserve.net/about-mahatma-gandhi/chronologies/chronology-1917/ |
| `ih-26-gandhi-and-noncooperation.u3.01` | `content/media/ih-26-gandhi-and-noncooperation/u3.01.webp` | https://gandhismriti.gov.in/more/chronology-mahatma-gandhi |
| `ih-26-gandhi-and-noncooperation.u3.02` | `content/media/ih-26-gandhi-and-noncooperation/u3.02.webp` | https://gorakhpur.nic.in/tourist-place/shaheed-smarak-chaurichaura/ |
| `ih-26-gandhi-and-noncooperation.u4.01` | `content/media/ih-26-gandhi-and-noncooperation/u4.01.webp` | https://inc.in/congress-sandesh/tribute/chittaranjan-das-and-swaraj-party, https://inc.in/leadership/past-party-presidents/motilal-nehru |
| `ih-26-gandhi-and-noncooperation.u4.02` | `content/media/ih-26-gandhi-and-noncooperation/u4.02.webp` | https://sansad.in/docs/flipbooks/Book/library/Guide_Parliament_House/files/basic-html/page11.html |
| `ih-27-simon-and-revolutionaries.u1.01` | `content/media/ih-27-simon-and-revolutionaries/u1.01.webp` |  |
| `ih-27-simon-and-revolutionaries.u1.02` | `content/media/ih-27-simon-and-revolutionaries/u1.02.webp` |  |
| `ih-27-simon-and-revolutionaries.u2.01` | `content/media/ih-27-simon-and-revolutionaries/u2.01.webp` |  |
| `ih-27-simon-and-revolutionaries.u2.02` | `content/media/ih-27-simon-and-revolutionaries/u2.02.webp` |  |
| `ih-27-simon-and-revolutionaries.u3.01` | `content/media/ih-27-simon-and-revolutionaries/u3.01.webp` | content/lessons/ih-27-simon-and-revolutionaries.json |
| `ih-27-simon-and-revolutionaries.u3.03` | `content/media/ih-27-simon-and-revolutionaries/u3.03.webp` | content/lessons/ih-27-simon-and-revolutionaries.json |
| `ih-28-salt-march.u1.01` | `content/media/ih-28-salt-march/u1.01.webp` | content/lessons/ih-28-salt-march.json |
| `ih-28-salt-march.u1.02` | `content/media/ih-28-salt-march/u1.02.webp` | content/lessons/ih-28-salt-march.json |
| `ih-28-salt-march.u3.01` | `content/media/ih-28-salt-march/u3.01.webp` | content/lessons/ih-28-salt-march.json |
| `ih-28-salt-march.u3.02` | `content/media/ih-28-salt-march/u3.02.webp` | content/lessons/ih-28-salt-march.json |
| `ih-28-salt-march.u3.03` | `content/media/ih-28-salt-march/u3.03.webp` | content/lessons/ih-28-salt-march.json |
| `ih-28-salt-march.u4.01` | `content/media/ih-28-salt-march/u4.01.webp` | content/lessons/ih-28-salt-march.json |
| `ih-28-salt-march.u4.02` | `content/media/ih-28-salt-march/u4.02.webp` | content/lessons/ih-28-salt-march.json |
| `ih-29-quit-india.u1.01` | `content/media/ih-29-quit-india/u1.01.webp` | content/lessons/ih-29-quit-india.json |
| `ih-29-quit-india.u2.01` | `content/media/ih-29-quit-india/u2.01.webp` | content/lessons/ih-29-quit-india.json |
| `ih-29-quit-india.u2.02` | `content/media/ih-29-quit-india/u2.02.webp` | content/lessons/ih-29-quit-india.json |
| `ih-29-quit-india.u3.01` | `content/media/ih-29-quit-india/u3.01.webp` | content/lessons/ih-29-quit-india.json |
| `ih-29-quit-india.u4.01` | `content/media/ih-29-quit-india/u4.01.webp` | content/lessons/ih-29-quit-india.json |
| `ih-30-bose-and-ina.u1.01` | `content/media/ih-30-bose-and-ina/u1.01.webp` | content/lessons/ih-30-bose-and-ina.json |
| `ih-30-bose-and-ina.u2.01` | `content/media/ih-30-bose-and-ina/u2.01.webp` | content/lessons/ih-30-bose-and-ina.json |
| `ih-30-bose-and-ina.u2.02` | `content/media/ih-30-bose-and-ina/u2.02.webp` | content/lessons/ih-30-bose-and-ina.json |
| `ih-30-bose-and-ina.u3.02` | `content/media/ih-30-bose-and-ina/u3.02.webp` | content/lessons/ih-30-bose-and-ina.json |
| `ih-31-road-to-1947.u1.01` | `content/media/ih-31-road-to-1947/u1.01.webp` | content/lessons/ih-31-road-to-1947.json |
| `ih-31-road-to-1947.u2.01` | `content/media/ih-31-road-to-1947/u2.01.webp` | content/lessons/ih-31-road-to-1947.json |
| `ih-31-road-to-1947.u2.02` | `content/media/ih-31-road-to-1947/u2.02.webp` | content/lessons/ih-31-road-to-1947.json |
| `ih-31-road-to-1947.u3.01` | `content/media/ih-31-road-to-1947/u3.01.webp` | content/lessons/ih-31-road-to-1947.json |
| `ih-31-road-to-1947.u3.02` | `content/media/ih-31-road-to-1947/u3.02.webp` | content/lessons/ih-31-road-to-1947.json |
| `ih-31-road-to-1947.u4.01` | `content/media/ih-31-road-to-1947/u4.01.webp` | content/lessons/ih-31-road-to-1947.json |
| `ih-31-road-to-1947.u4.02` | `content/media/ih-31-road-to-1947/u4.02.webp` | content/lessons/ih-31-road-to-1947.json |
| `ih-32-building-the-republic.u1.01` | `content/media/ih-32-building-the-republic/u1.01.webp` | content/lessons/ih-32-building-the-republic.json |
| `ih-32-building-the-republic.u1.02` | `content/media/ih-32-building-the-republic/u1.02.webp` | content/lessons/ih-32-building-the-republic.json |
| `ih-32-building-the-republic.u2.01` | `content/media/ih-32-building-the-republic/u2.01.webp` | content/lessons/ih-32-building-the-republic.json |
| `ih-32-building-the-republic.u2.02` | `content/media/ih-32-building-the-republic/u2.02.webp` | content/lessons/ih-32-building-the-republic.json |
| `ih-32-building-the-republic.u3.01` | `content/media/ih-32-building-the-republic/u3.01.webp` | content/lessons/ih-32-building-the-republic.json |
| `ih-32-building-the-republic.u4.01` | `content/media/ih-32-building-the-republic/u4.01.webp` | content/lessons/ih-32-building-the-republic.json |
