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
  customerOutcomes,
  installedSystem,
  processSteps,
  siteMeta,
  solutionModel,
  sunparkResponsibilities,
} from "@/content/site";
import { assertSourceNotes } from "@/content/sourceGuard";

export const metadata: Metadata = {
  title: "Solution",
  description:
    "How SunPark delivers solar carports without upfront capex for commercial sites in Morocco.",
};

export default function SolutionPage() {
  assertSourceNotes();

  return (
    <>
      <HeroBand
        body="SunPark makes solar adoption operationally simple: we fund, own, and run the carport while your site buys the generated electricity through a long-term PPA."
        eyebrow="Solution"
        primaryCta={{ label: "Check whether your site is suitable", href: "/contact" }}
        secondaryCta={{ label: "View the process", href: "/process" }}
        title="Solar carports with zero upfront capex."
      />

      <SectionShell>
        <div className="split-layout">
          <div className="section-intro">
            <p className="eyebrow">The customer problem</p>
            <h2 className="type-display-md">
              Solar can lower energy costs, but ownership complexity slows action.
            </h2>
            <p>
              The source documents identify a recurring pattern across
              commercial solar projects: customers may want lower-cost power,
              but financing, asset ownership, maintenance responsibility, and
              landlord-tenant complexity turn solar into a heavy infrastructure
              decision.
            </p>
          </div>
          <SignatureCard tone="cream">
            <h3 className="type-display-md">
              SunPark removes ownership burden from your team.
            </h3>
            <p className="signature-card__copy">
              The customer does not buy the carport. SunPark owns and operates
              the system, and the site buys electricity from the asset under a
              PPA.
            </p>
          </SignatureCard>
        </div>
      </SectionShell>

      <SectionShell compact>
        <div className="section-intro">
          <p className="eyebrow">The SunPark model</p>
          <h2 className="type-display-md">
            Energy procurement instead of asset procurement.
          </h2>
        </div>
        <div className="flow-row">
          {solutionModel.map((item) => (
            <article className="flow-card" key={item.title}>
              <h3 className="type-title-sm">{item.title}</h3>
              <p>{item.body}</p>
            </article>
          ))}
        </div>
      </SectionShell>

      <SectionShell>
        <div className="section-intro">
          <p className="eyebrow">What gets installed</p>
          <h2 className="type-display-md">
            A modular carport system designed around commercial parking.
          </h2>
          <p>
            The source architecture is practical and infrastructure-grade:
            canopy structure, solar generation hardware, monitoring, and
            readiness for future EV charging integration.
          </p>
        </div>
        <ResponsiveGrid columns={2}>
          {installedSystem.map((item) => (
            <article className="mini-card" key={item.title}>
              <h3 className="type-title-sm">{item.title}</h3>
              <p>{item.body}</p>
            </article>
          ))}
        </ResponsiveGrid>
      </SectionShell>

      <SectionShell>
        <div className="split-layout">
          <div>
            <div className="section-intro">
              <p className="eyebrow">What the customer gets</p>
              <h2 className="type-display-md">
                Cleaner electricity, shaded parking, and less internal workload.
              </h2>
            </div>
            <div className="stack">
              {customerOutcomes.map((item) => (
                <article className="mini-card mini-card--soft" key={item.title}>
                  <h3 className="type-title-sm">{item.title}</h3>
                  <p>{item.body}</p>
                </article>
              ))}
            </div>
          </div>
          <div>
            <div className="section-intro">
              <p className="eyebrow">What SunPark handles</p>
              <h2 className="type-display-md">
                The workstreams behind a credible energy-service project.
              </h2>
            </div>
            <div className="responsibility-list">
              {sunparkResponsibilities.map((item) => (
                <article className="comparison-card" key={item.title}>
                  <h3 className="type-title-sm">{item.title}</h3>
                  <p>{item.body}</p>
                </article>
              ))}
            </div>
          </div>
        </div>
      </SectionShell>

      <SectionShell compact>
        <div className="section-intro">
          <p className="eyebrow">Delivery path</p>
          <h2 className="type-display-md">
            From first assessment to long-term service.
          </h2>
        </div>
        <ProcessTimeline steps={processSteps} />
      </SectionShell>

      <SectionShell>
        <div className="cta-band-light">
          <p className="eyebrow">Assess a site</p>
          <h2 className="type-display-md">
            Find out whether your parking area is suitable.
          </h2>
          <p className="signature-card__copy">
            Start with a commercial parking site, its energy needs, and the
            ownership context. SunPark can then assess whether a managed solar
            carport PPA is a fit.
          </p>
          <div className="button-row">
            <Button href="/contact">{siteMeta.primaryCta}</Button>
            <Button href="/sectors" variant="secondary">
              Explore sectors
            </Button>
          </div>
        </div>
      </SectionShell>
    </>
  );
}
