import type { Metadata } from "next";
import {
  Button,
  FAQAccordion,
  HeroBand,
  ResponsiveGrid,
  SectionShell,
  SignatureCard,
} from "@/components";
import {
  faqItems,
  ppaExplainers,
  siteMeta,
} from "@/content/site";
import { assertSourceNotes } from "@/content/sourceGuard";

export const metadata: Metadata = {
  title: "FAQ",
  description:
    "Clear answers for commercial site owners considering SunPark solar carports.",
};

export default function FAQPage() {
  assertSourceNotes();

  return (
    <>
      <HeroBand
        body="Clear answers on ownership, upfront cost, PPAs, maintenance, land use, EV-readiness, and the Law 82-21 framework behind SunPark."
        eyebrow="FAQ"
        primaryCta={{ label: "Ask about your site", href: "/contact" }}
        secondaryCta={{ label: "Explore the process", href: "/process" }}
        title="Clear answers for commercial decision-makers."
      />

      <SectionShell>
        <div className="split-layout">
          <div className="section-intro">
            <p className="eyebrow">Customer questions</p>
            <h2 className="type-display-md">
              What a site owner or operator usually needs to know first.
            </h2>
            <p>
              These answers are rewritten from source material for a public
              website audience. They intentionally remove investor challenge
              framing and focus on practical customer clarity.
            </p>
          </div>
          <FAQAccordion items={faqItems} />
        </div>
      </SectionShell>

      <SectionShell compact>
        <div className="section-intro">
          <p className="eyebrow">Short explainers</p>
          <h2 className="type-display-md">
            Three fundamentals behind the SunPark model.
          </h2>
        </div>
        <ResponsiveGrid>
          {ppaExplainers.map((item) => (
            <article className="mini-card" key={item.title}>
              <h3 className="type-title-sm">{item.title}</h3>
              <p>{item.body}</p>
            </article>
          ))}
        </ResponsiveGrid>
      </SectionShell>

      <SectionShell>
        <SignatureCard tone="cream">
          <p className="eyebrow">Still evaluating fit?</p>
          <h2 className="type-display-md">
            The right first step is a site-specific conversation.
          </h2>
          <p className="signature-card__copy">
            SunPark needs to understand the parking area, ownership structure,
            and energy context before recommending whether a solar carport PPA
            is appropriate.
          </p>
          <div className="button-row">
            <Button href="/contact" variant="secondary">
              Get in touch
            </Button>
            <Button href="/solution" variant="secondary">
              See the solution
            </Button>
          </div>
        </SignatureCard>
      </SectionShell>
    </>
  );
}
