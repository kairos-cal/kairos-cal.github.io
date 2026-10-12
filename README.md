# kairos-cal.github.io

The public website of [Kairos](https://kairos-cal.coding-pit.com): the landing page and the privacy
policy and terms of service that Google's OAuth consent screen links to. English at `/`, Spanish
at `/es/`.

| Page | English | Spanish |
|---|---|---|
| Home | `/` | `/es/` |
| Privacy policy | `/privacy/` | `/es/privacy/` |
| Terms of service | `/terms/` | `/es/terms/` |

The privacy and terms URLs are entered in Google Cloud's consent screen. **Do not move or rename
them** without updating the consent screen first.

## Develop

```sh
npm install
npm run dev      # http://localhost:4321
npm run check    # type-check the .astro files
npm run build    # static site in dist/
```

Every push to `main` builds and deploys to GitHub Pages (`.github/workflows/deploy.yml`); pull
requests only build.

## Editing the legal pages

The operator's name, contact email and the service URL live in one place, `src/i18n.ts`
(`operator`). When either document changes in substance, bump `legalUpdated` in the same file,
change both languages in the same commit, and tell Hosts by email before it takes effect — both
documents promise that.

The privacy policy describes what the Kairos code actually does (scopes, stored fields, retention).
If Kairos changes what it stores or asks Google for, this page changes in the same release.

## Logo

`brand/logo-source.jpg` is the master. Every icon in `public/` is derived from it:

```sh
npm run icons    # uv run --with pillow python3 scripts/make-icons.py public
```

`public/consent-logo-120.png` is the 120×120 file uploaded to Google's consent screen.

## Domain

Served by GitHub Pages at **https://kairos-cal.coding-pit.com** (custom domain; `kairos-cal.github.io`
redirects to it). Google's OAuth brand verification requires a homepage on a domain we own, which
`github.io` is not. DNS lives at Nominalia: `CNAME kairos-cal -> kairos-cal.github.io.` plus GitHub's
`_github-pages-challenge-kairos-cal.kairos-cal` TXT, which proves the domain to the `kairos-cal`
organisation so nobody else can claim it. The domain moves again when `coding-pit.com` is scrubbed
before the code goes public (juanjecilla/kairos#47).

## Google Search Console

Ownership is proven by the `coding-pit.com` **Domain** property (DNS TXT, already in place), which
covers every subdomain, so no meta tag is needed. `PUBLIC_GOOGLE_SITE_VERIFICATION` is kept as an
optional fallback: put a token from Search Console's *HTML tag* method in the repository variable
`GOOGLE_SITE_VERIFICATION` and re-run the deploy; the layout renders the
`<meta name="google-site-verification">` tag only when it is set.
