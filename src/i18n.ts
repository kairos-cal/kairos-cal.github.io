export const locales = ['en', 'es'] as const;
export type Lang = (typeof locales)[number];

/** Who runs the service and how to reach them. One place, because the policy, the terms and the
 * footer must never disagree. */
export const operator = {
  name: 'Juan Jesús Cilla',
  email: 'scallop.projects@gmail.com',
  appUrl: 'https://kairos.coding-pit.com',
};

/** Last substantive change to the legal documents, shown on both. */
export const legalUpdated = '2026-09-26';

const ui = {
  en: {
    tagline: 'Scheduling for groups who all need to be there.',
    description:
      'Kairos books sessions only when every host is free and has said yes to that time. Hosts connect their calendars and offer times; guests pick from what everyone agreed.',
    nav: { home: 'Home', privacy: 'Privacy', terms: 'Terms' },
    footer: {
      privacy: 'Privacy policy',
      terms: 'Terms of service',
      contact: 'Contact',
      operatedBy: 'Operated by',
    },
    langName: 'English',
    otherLang: 'Español',
    updated: 'Last updated',
  },
  es: {
    tagline: 'Agenda para grupos que tienen que estar todos.',
    description:
      'Kairos solo reserva una sesión cuando todos los anfitriones están libres y han aceptado ese horario. Los anfitriones conectan sus calendarios y ofrecen horarios; los invitados eligen entre lo que todos acordaron.',
    nav: { home: 'Inicio', privacy: 'Privacidad', terms: 'Condiciones' },
    footer: {
      privacy: 'Política de privacidad',
      terms: 'Condiciones del servicio',
      contact: 'Contacto',
      operatedBy: 'Gestionado por',
    },
    langName: 'Español',
    otherLang: 'English',
    updated: 'Última actualización',
  },
} as const;

export function t(lang: Lang) {
  return ui[lang];
}

/** The path of a page in the given language: English at the root, Spanish under /es/. */
export function localePath(lang: Lang, page: '' | 'privacy' | 'terms'): string {
  const prefix = lang === 'en' ? '/' : '/es/';
  return page ? `${prefix}${page}/` : prefix;
}

export function formatDate(lang: Lang, iso: string): string {
  return new Date(`${iso}T12:00:00Z`).toLocaleDateString(lang === 'en' ? 'en-GB' : 'es-ES', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  });
}
