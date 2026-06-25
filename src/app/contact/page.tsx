import type { Metadata } from "next";
import {
  ContactForm,
  HeroBand,
  ResponsiveGrid,
  SectionShell,
  SignatureCard,
} from "@/components";
import { contactFields, sectors } from "@/content/site";
import { assertSourceNotes } from "@/content/sourceGuard";

export const metadata: Metadata = {
  title: "Contact",
  description:
    "Discuss a Moroccan commercial parking site, partnership, financing, EPC, or advisory conversation with SunPark.",
};

export default function ContactPage() {
  assertSourceNotes();

  return (
    <>
      <HeroBand
        body="Share your site context and what you want to evaluate. SunPark can quickly assess whether a managed solar carport PPA is a fit."
        eyebrow="Contact"
        title="Start with your commercial parking site."
      />

      <SectionShell>
        <div className="split-layout">
          <div className="section-intro">
            <p className="eyebrow">Who should get in touch</p>
            <h2 className="type-display-md">
              Commercial site owners, operators, and project partners.
            </h2>
            <p>
              SunPark is designed for commercial parking assets in Morocco
              across retail, logistics, hospitality, and office sites. The same
              form can also support conversations with EPC partners, green
              lenders, energy advisors, and legal advisors.
            </p>
          </div>

          <SignatureCard tone="cream">
            <p className="eyebrow">What helps at the first step</p>
            <h3 className="type-display-md">
              Site type, location, parking capacity, and commercial objective.
            </h3>
            <p className="signature-card__copy">
              SunPark can assess fit more clearly when the enquiry includes the
              property type, city, approximate parking spaces, and whether the
              conversation is about feasibility, PPA structure, partnership, or
              advisory support.
            </p>
          </SignatureCard>
        </div>
      </SectionShell>

      <SectionShell compact>
        <div className="section-intro">
          <p className="eyebrow">Qualification form</p>
          <h2 className="type-display-md">
            Share enough context for a useful first conversation.
          </h2>
        </div>
        <ContactForm fields={contactFields} />
      </SectionShell>

      <SectionShell>
        <div className="section-intro">
          <p className="eyebrow">Site categories</p>
          <h2 className="type-display-md">
            The form is structured around SunPark&apos;s approved target sectors.
          </h2>
        </div>
        <ResponsiveGrid>
          {sectors.map((sector) => (
            <article className="mini-card mini-card--soft" key={sector.name}>
              <h3 className="type-title-sm">{sector.name}</h3>
              <p>{sector.body}</p>
            </article>
          ))}
        </ResponsiveGrid>
      </SectionShell>
    </>
  );
}
