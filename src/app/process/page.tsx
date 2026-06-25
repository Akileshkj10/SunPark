import type { Metadata } from "next";
import {
  Button,
  HeroBand,
  ProcessTimeline,
  ResponsiveGrid,
  SectionShell,
  SignatureCard,
} from "@/components";
import {
  operationsAfterLaunch,
  processResponsibilities,
  processSteps,
  regulatorySupport,
  siteMeta,
} from "@/content/site";
import { assertSourceNotes } from "@/content/sourceGuard";

export const metadata: Metadata = {
  title: "Process",
  description:
    "A clear path from commercial parking assessment to clean power with SunPark.",
};

export default function ProcessPage() {
  assertSourceNotes();

  return (
    <>
      <HeroBand
        body="SunPark reduces project friction by sequencing feasibility, commercial structure, regulatory coordination, delivery, and operations into one managed path."
        eyebrow="Process"
        primaryCta={{ label: "Start a feasibility conversation", href: "/contact" }}
        secondaryCta={{ label: "Explore the solution", href: "/solution" }}
        title="From parking assessment to live clean generation."
      />

      <SectionShell>
        <div className="section-intro">
          <p className="eyebrow">Delivery timeline</p>
          <h2 className="type-display-md">
            The sequence is designed to reduce risk before build starts.
          </h2>
          <p>
            The steps below are presented as a delivery sequence, not guaranteed
            approval or construction timelines. Regulatory and grid coordination
            remain project-specific dependencies.
          </p>
        </div>
        <ProcessTimeline steps={processSteps} />
      </SectionShell>

      <SectionShell compact>
        <div className="section-intro">
          <p className="eyebrow">Responsibilities</p>
          <h2 className="type-display-md">
            Keep customer decisions simple while specialist work runs in the background.
          </h2>
        </div>
        <ResponsiveGrid>
          {processResponsibilities.map((item) => (
            <article className="mini-card" key={item.title}>
              <h3 className="type-title-sm">{item.title}</h3>
              <p>{item.body}</p>
            </article>
          ))}
        </ResponsiveGrid>
      </SectionShell>

      <SectionShell>
        <div className="split-layout">
          <SignatureCard tone="cream">
            <p className="eyebrow">Regulatory support</p>
            <h2 className="type-display-md">
              Law 82-21 makes the model possible, but execution still needs care.
            </h2>
            <p className="signature-card__copy">
              SunPark treats regulatory and grid coordination as a core project
              workstream. The site should understand the pathway clearly before
              installation begins.
            </p>
          </SignatureCard>
          <div className="stack">
            {regulatorySupport.map((item) => (
              <article className="comparison-card" key={item.title}>
                <h3 className="type-title-sm">{item.title}</h3>
                <p>{item.body}</p>
              </article>
            ))}
          </div>
        </div>
      </SectionShell>

      <SectionShell compact>
        <div className="section-intro">
          <p className="eyebrow">After launch</p>
          <h2 className="type-display-md">
            The service continues after commissioning.
          </h2>
        </div>
        <ResponsiveGrid>
          {operationsAfterLaunch.map((item) => (
            <article className="mini-card mini-card--soft" key={item.title}>
              <h3 className="type-title-sm">{item.title}</h3>
              <p>{item.body}</p>
            </article>
          ))}
        </ResponsiveGrid>
      </SectionShell>

      <SectionShell>
        <div className="cta-band-light">
          <p className="eyebrow">Start with the site</p>
          <h2 className="type-display-md">
            Bring the parking layout, ownership context, and energy needs.
          </h2>
          <p className="signature-card__copy">
            SunPark can then assess whether the site is a fit for a managed
            solar carport PPA.
          </p>
          <div className="button-row">
            <Button href="/contact">{siteMeta.primaryCta}</Button>
            <Button href="/sectors" variant="secondary">
              View sectors
            </Button>
          </div>
        </div>
      </SectionShell>
    </>
  );
}
