## Ripcord
🇱🇻 Platforma, kur studenti dalās ar kvalitatīviem studiju resursiem un palīgmateriāliem.

🇬🇧 Platform for students to share quality study resources and guides.

Autors/Author: Jēkabs G.

## Apraksts / Description

🇬🇧
---
Students often make some of the best teachers. Their knowledge of a subject is not only more recent, but their shared perspective makes it easier to connect with a peer and meet them where they are.

Because of this, it's no secret that many intuitive study resources come not from official materials, books, and documentation, but from peers and recent graduates. Unfortunately, these resources are often scattered across various corners of the internet and obscure Discord servers.

_Ripcord aims to fix that_ - is what I would say [were I more naive](https://xkcd.com/927/). In reality, this is just a means to complete an assignment with a non-trivial database implementation.

🇱🇻
---
Studenti bieži vien ir vieni no labākajiem skolotājiem. Viņu zināšanas par priekšmetu ir ne tikai jaunākas, bet arī kopīgā perspektīva ļauj brīvāk iejusties viņu situācijā.

Tāpēc nav noslēpums, ka visintuitīvākie mācību resursi nāk nevis no oficiāliem materiāliem, grāmatām un dokumentācijas, bet gan no vienaudžiem un absolventiem. Diemžēl šie resursi bieži vien ir izkaisīti pa dažādiem interneta nostūriem un mazizplatītiem Discord serveriem.

_Ripcord mērķis ir to mainīt_ - vismaz tā es teiktu, [ja būtu naivāks](https://xkcd.com/927/). Patiesībā, šis ir tikai iesniegums praktiskajam darbam ar netriviālu datubāzes implementāciju.

## Instrukcijas / Usage guide

🇬🇧
---
1. Install dependencies: `git` and `python`.
2. Clone this repository and enter its root directory.
3. Create and enter a Python virtual environment (optional):
  - 1. `python -m venv .venv`
  - 2. `source .venv/bin/activate`
4. Enter `ripcord_web` and migrate the database:
  - 1. `cd ripcord_web`
  - 2. `python manage.py migrate`
5. Create a superuser account:
  - 1. `python manage.py createsuperuser`
6. Start the server:
  - 1. `python manage.py runserver`

🇱🇻
---
1. Instalē `git` un `python`.
2. Klonē šo repozitoriju un ieej tās mapē.
3. Izveido un aktivizē Python virtuālo vidi (neobligāti):
  - 1. `python -m venv .venv`
  - 2. `source .venv/bin/activate`
4. Ieej `ripcord_web` mapē un migrē datubāzi:
  - 1. `cd ripcord_web`
  - 2. `python manage.py migrate`
5. Izveido administratora profilu:
  - 1. `python manage.py createsuperuser`
6. Palaid serveri:
  - 1. `python manage.py runserver`
