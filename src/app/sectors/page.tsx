import type { Metadata } from "next";
import {
  Button,
  HeroBand,
  ResponsiveGrid,
  SectionShell,
  SectorCard,
  SignatureCard,
} from "@/components";
import {
  multiSiteExpansion,
  sectors,
  siteMeta,
} from "@/content/site";
import { assertSourceNotes } from "@/content/sourceGuard";

export const metadata: Metadata = {
  title: "Sectors",
  description:
    "SunPark is designed for commercial parking assets across retail, logistics, hospitality, and office sites in Morocco.",
};

export default function SectorsPage() {
  assertSourceNotes();

  return (
    <>
      <HeroBand
        body="SunPark is built for commercial parking assets where energy cost pressure and customer experience matter. Across sectors, the value stays consistent: no upfront capex, shaded parking, and clean electricity through a managed PPA."
        eyebrow="Sectors"
        primaryCta={{ label: siteMeta.primaryCta, href: "/contact" }}
        secondaryCta={{ label: "How the process works", href: "/process" }}
        title="Built for Morocco's commercial parking assets."
      />

      <SectionShell compact>
        <ResponsiveGrid>
          {sectors.map((sector) => (
            <SectorCard key={sector.name} sector={sector} />
          ))}
        </ResponsiveGrid>
      </SectionShell>

      <SectionShell>
        <div className="section-intro">
          <p className="eyebrow">Sector fit</p>
          <h2 className="type-display-md">
            Different properties, one clear energy model.
          </h2>
          <p>
            The site types below are drawn from the source documents. SunPark
            should not present any of them as existing customers unless that
            proof is supplied later.
          </p>
        </div>

        <div>
          {sectors.map((sector) => (
            <article className="sector-detail" key={sector.name}>
              <div>
                <p className="type-caption sector-detail__meta">{sector.name}</p>
                <h3 className="type-display-md">{sector.headline}</h3>
              </div>
              <div className="stack">
                <p>{sector.body}</p>
                <div className="flow-row">
                  {sector.suitability.map((item) => (
                    <div className="flow-card" key={item}>
                      <p className="type-label-md">{item}</p>
                    </div>
                  ))}
                </div>
              </div>
            </article>
          ))}
        </div>
      </SectionShell>

      <SectionShell>
        <div className="split-layout">
          <SignatureCard tone="dark">
            <p className="eyebrow">Multi-site expansion</p>
            <h2 className="type-display-md">
              One framework can speed up future site decisions.
            </h2>
            <p className="signature-card__copy">
              SunPark is designed for repeatable commercial structures, so a
              customer with more than one site does not need to restart the
              entire solar ownership conversation each time.
            </p>
          </SignatureCard>

          <div className="stack">
            {multiSiteExpansion.map((item) => (
              <article className="mini-card mini-card--soft" key={item.title}>
                <h3 className="type-title-sm">{item.title}</h3>
                <p>{item.body}</p>
              </article>
            ))}
          </div>
        </div>
      </SectionShell>

      <SectionShell>
        <div className="cta-band-light">
          <p className="eyebrow">Start with one site</p>
          <h2 className="type-display-md">
            Assess whether your parking asset is suitable for SunPark.
          </h2>
          <p className="signature-card__copy">
            A useful first conversation covers site type, parking capacity,
            ownership context, and electricity demand.
          </p>
          <div className="button-row">
            <Button href="/contact">{siteMeta.primaryCta}</Button>
            <Button href="/solution" variant="secondary">
              See the solution
            </Button>
          </div>
        </div>
      </SectionShell>
    </>
  );
}
