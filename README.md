# kairos-cal.github.io

The public website of [Kairos](https://kairos-cal.github.io): the landing page and the privacy
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

## Google Search Console

Brand verification needs this site's ownership proven. Put the token from Search Console's
*HTML tag* method in the repository variable `GOOGLE_SITE_VERIFICATION`
(Settings → Secrets and variables → Actions → Variables) and re-run the deploy; the layout
renders the `<meta name="google-site-verification">` tag only when it is set.
