import type { Metadata } from "next";
import {
  Button,
  HeroBand,
  ResponsiveGrid,
  SectionShell,
  SignatureCard,
} from "@/components";
import {
  operatingPrinciples,
  siteMeta,
  specialistSupport,
  teamRoles,
} from "@/content/site";
import { assertSourceNotes } from "@/content/sourceGuard";

export const metadata: Metadata = {
  title: "Company",
  description:
    "SunPark is a Morocco-focused clean infrastructure company built around commercial, technical, regulatory, finance, and partnership execution.",
};

export default function CompanyPage() {
  assertSourceNotes();

  return (
    <>
      <HeroBand
        body="SunPark exists to make commercial solar adoption simpler in Morocco: zero upfront capex for customers, a managed PPA structure, and long-term operations handled by SunPark."
        eyebrow="Company"
        primaryCta={{ label: siteMeta.primaryCta, href: "/contact" }}
        secondaryCta={{ label: "See the solution", href: "/solution" }}
        title="A Morocco-focused clean infrastructure operator."
      />

      <SectionShell>
        <div className="split-layout">
          <SignatureCard tone="forest">
            <p className="eyebrow">Mission</p>
            <h2 className="type-display-md">
              Turn underused commercial parking into clean energy infrastructure.
            </h2>
            <p className="signature-card__copy">
              SunPark does this without asking customers to carry the upfront
              ownership and maintenance burden that has slowed commercial solar
              adoption.
            </p>
          </SignatureCard>
          <div className="section-intro">
            <p className="eyebrow">Why SunPark exists</p>
            <h2 className="type-display-md">
              Morocco has the solar conditions. Commercial sites need a simpler route.
            </h2>
            <p>
              The source documents identify strong solar potential, rising
              commercial energy pressure, and a new legal framework. The gap is
              practical adoption: financing, ownership, and contractual
              complexity still stop many projects before they start.
            </p>
          </div>
        </div>
      </SectionShell>

      <SectionShell compact>
        <div className="section-intro">
          <p className="eyebrow">Operating principles</p>
          <h2 className="type-display-md">
            Built for repeatable and dependable execution.
          </h2>
        </div>
        <ResponsiveGrid columns={2}>
          {operatingPrinciples.map((principle) => (
            <article className="mini-card" key={principle.title}>
              <h3 className="type-title-sm">{principle.title}</h3>
              <p>{principle.body}</p>
            </article>
          ))}
        </ResponsiveGrid>
      </SectionShell>

      <SectionShell>
        <div className="section-intro">
          <p className="eyebrow">Team structure</p>
          <h2 className="type-display-md">
            Each founder owns one critical workstream.
          </h2>
          <p>
            The company is presented by role ownership rather than inflated
            biography. That keeps the page honest and aligned with the source
            documents.
          </p>
        </div>
        <div className="team-grid">
          {teamRoles.map((member) => (
            <article className="team-card" key={member.name}>
              <span className="team-card__initial">{member.name[0]}</span>
              <h3 className="type-title-sm">{member.name}</h3>
              <p className="type-caption">{member.role}</p>
              <p>{member.responsibility}</p>
            </article>
          ))}
        </div>
      </SectionShell>

      <SectionShell>
        <div className="split-layout">
          <div className="section-intro">
            <p className="eyebrow">Specialist support</p>
            <h2 className="type-display-md">
              Lean core team, specialist depth where execution quality matters.
            </h2>
            <p>
              SunPark source material uses contracted specialist support rather
              than overstating full-time internal capability at this stage.
            </p>
          </div>
          <div className="stack">
            {specialistSupport.map((support) => (
              <article className="comparison-card" key={support.title}>
                <h3 className="type-title-sm">{support.title}</h3>
                <p>{support.body}</p>
              </article>
            ))}
          </div>
        </div>
      </SectionShell>

      <SectionShell>
        <div className="cta-band-light">
          <p className="eyebrow">Work with SunPark</p>
          <h2 className="type-display-md">
            Commercial site owner, operator, lender, advisor, or EPC partner?
          </h2>
          <p className="signature-card__copy">
            SunPark is built around the commercial and technical work required
            to turn parking assets into long-term clean energy infrastructure.
          </p>
          <div className="button-row">
            <Button href="/contact">{siteMeta.primaryCta}</Button>
            <Button href="/process" variant="secondary">
              View the process
            </Button>
          </div>
        </div>
      </SectionShell>
    </>
  );
}
