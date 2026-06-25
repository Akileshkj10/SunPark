export type SourceDocument =
  | "Entrepreneurship Doc (1).pdf"
  | "SunPark_Deck_GBP.pptx (1).pptx"
  | "DESIGN-airtable.md";

export type SourceNote = {
  document: SourceDocument;
  locator: string;
  evidence: string;
};

export type SourcedText = {
  publicText: string;
  sourceNotes: SourceNote[];
};

export type NavItem = {
  label: string;
  href: string;
};

export type Metric = {
  value: string;
  label: string;
  context: string;
  sourceNotes: SourceNote[];
};

export type Sector = {
  name: string;
  headline: string;
  body: string;
  suitability: string[];
  sourceNotes: SourceNote[];
};

export type ProcessStep = {
  title: string;
  body: string;
  sourceNotes: SourceNote[];
};

export type TeamRole = {
  name: string;
  role: string;
  responsibility: string;
  sourceNotes: SourceNote[];
};

export type FAQItem = {
  question: string;
  answer: string;
  sourceNotes: SourceNote[];
};

export type FormField = {
  name: string;
  label: string;
  type: "text" | "email" | "tel" | "select" | "textarea";
  required?: boolean;
  options?: string[];
};
