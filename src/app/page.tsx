import {
  BenefitCard,
  Button,
  HeroBand,
  MetricStrip,
  ResponsiveGrid,
  SectionShell,
  SectorCard,
  SignatureCard,
} from "@/components";
import {
  benefits,
  howItWorksPreview,
  moroccoContext,
  publicMetrics,
  positioning,
  sectors,
  siteMeta,
  teamRoles,
} from "@/content/site";
import { assertSourceNotes } from "@/content/sourceGuard";

export default function Home() {
  assertSourceNotes();

  return (
    <>
      <HeroBand
        body={positioning.publicText}
        eyebrow="Solar Carport as a Service"
        primaryCta={{ label: "Get in touch", href: "/contact" }}
        secondaryCta={{ label: siteMeta.secondaryCta, href: "/process" }}
        title="Turn parking assets into reliable, lower-cost clean power."
      >
        <div className="visual-card">
          <p className="type-caption">Example project preview</p>
          <div className="mockup-shell" aria-hidden="true">
            <div className="mockup-shell__row">
              <span className="type-caption">Site screening</span>
              <span className="mockup-shell__slot">Ready</span>
            </div>
            <div className="mockup-shell__row">
              <span className="type-caption">PPA structure</span>
              <span className="mockup-shell__slot">In review</span>
            </div>
            <div className="mockup-shell__row">
              <span className="type-caption">Build + commissioning</span>
              <span className="mockup-shell__slot">Planned</span>
            </div>
            <div className="mockup-shell__row">
              <span className="type-caption">Operations handover</span>
              <span className="mockup-shell__slot">Managed</span>
            </div>
          </div>
        </div>
      </HeroBand>

      <SectionShell compact>
        <ResponsiveGrid columns={2}>
          {benefits.map((benefit) => (
            <BenefitCard
              body={benefit.body}
              key={benefit.title}
              title={benefit.title}
            />
          ))}
        </ResponsiveGrid>
      </SectionShell>

      <SectionShell>
        <div className="split-layout">
          <div className="section-intro">
            <p className="eyebrow">What SunPark builds</p>
            <h2 className="type-display-md">
              Keep parking operational while it starts producing value.
            </h2>
            <p>
              SunPark installs modular solar canopies over existing commercial parking.
              The site keeps serving vehicles while adding shade and on-site generation.
            </p>
          </div>
          <SignatureCard tone="forest">
            <h3 className="type-display-md">A practical energy contract, not an ownership burden.</h3>
            <p className="signature-card__copy">
              The customer does not need to own, finance, or maintain the
              infrastructure. SunPark owns and operates the asset, and the site
              buys generated electricity through a long-term PPA.
            </p>
          </SignatureCard>
        </div>
      </SectionShell>

      <SectionShell compact>
        <div className="section-intro">
          <p className="eyebrow">How it works</p>
          <h2 className="type-display-md">A clear path from first review to live generation.</h2>
        </div>
        <ResponsiveGrid columns={2}>
          {howItWorksPreview.map((step, index) => (
            <article className="mini-card" key={step.title}>
              <span className="type-caption mini-card__index">
                {String(index + 1).padStart(2, "0")}
              </span>
              <h3 className="type-title-sm">{step.title}</h3>
              <p>{step.body}</p>
            </article>
          ))}
        </ResponsiveGrid>
      </SectionShell>

      <SectionShell>
        <div className="split-layout">
          <SignatureCard tone="cream">
            <p className="eyebrow">Why Morocco, why now</p>
            <h2 className="type-display-md">
              Strong solar potential now has a clearer commercial framework.
            </h2>
          </SignatureCard>
          <div className="stack">
            {moroccoContext.map((item) => (
              <article className="mini-card mini-card--soft" key={item.title}>
                <h3 className="type-title-sm">{item.title}</h3>
                <p>{item.body}</p>
              </article>
            ))}
          </div>
        </div>
      </SectionShell>

      <SectionShell compact>
        <div className="section-intro">
          <p className="eyebrow">Customer economics</p>
          <h2 className="type-display-md">
            Commercial value is clear from day one.
          </h2>
          <p>
            These public figures are used carefully from the source model. They
            describe the customer proposition and technical scale, not investor
            returns.
          </p>
        </div>
        <MetricStrip metrics={publicMetrics} />
      </SectionShell>

      <SectionShell>
        <div className="section-intro">
          <p className="eyebrow">Built for commercial sites</p>
          <h2 className="type-display-md">
            Retail, logistics, hospitality, and office parking assets.
          </h2>
        </div>
        <ResponsiveGrid>
          {sectors.map((sector) => (
            <SectorCard key={sector.name} sector={sector} />
          ))}
        </ResponsiveGrid>
      </SectionShell>

      <SectionShell>
        <div className="split-layout">
          <div className="section-intro">
            <p className="eyebrow">Trust and execution</p>
            <h2 className="type-display-md">
              Built around the execution that makes infrastructure reliable.
            </h2>
            <p>
              SunPark is structured around commercial, finance, technical,
              regulatory, and partnership responsibilities. The website keeps
              this grounded in role ownership rather than inflated biographies.
            </p>
          </div>
          <div className="team-grid">
            {teamRoles.map((member) => (
              <article className="team-card" key={member.name}>
                <span className="team-card__initial">{member.name[0]}</span>
                <h3 className="type-title-sm">{member.name}</h3>
                <p className="type-caption">{member.role}</p>
              </article>
            ))}
          </div>
        </div>
      </SectionShell>

      <SectionShell>
        <div className="cta-band-light">
          <p className="eyebrow">Start with a site assessment</p>
          <h2 className="type-display-md">
            Have a commercial parking site in Morocco?
          </h2>
          <p className="signature-card__copy">
            SunPark can help assess whether the site is suitable for a solar
            carport and long-term clean electricity PPA.
          </p>
          <div className="button-row">
            <Button href="/contact">Get in touch</Button>
            <Button href="/solution" variant="secondary">
              Explore the solution
            </Button>
          </div>
        </div>
      </SectionShell>
    </>
  );
}
