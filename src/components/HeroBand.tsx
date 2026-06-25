import type { ReactNode } from "react";
import { Button } from "./Button";

type HeroBandProps = {
  eyebrow?: string;
  title: string;
  body: string;
  primaryCta?: {
    label: string;
    href: string;
  };
  secondaryCta?: {
    label: string;
    href: string;
  };
  children?: ReactNode;
};

export function HeroBand({
  eyebrow,
  title,
  body,
  primaryCta,
  secondaryCta,
  children,
}: HeroBandProps) {
  return (
    <section className="hero-band">
      <div className={children ? "hero-band__inner hero-band__inner--with-aside" : "hero-band__inner"}>
        <div className="hero-band__main">
          {eyebrow ? <p className="eyebrow">{eyebrow}</p> : null}
          <h1 className="type-display-lg hero-band__title">{title}</h1>
          <p className="type-title-lg hero-band__copy">{body}</p>
          {primaryCta || secondaryCta ? (
            <div className="button-row">
              {primaryCta ? <Button href={primaryCta.href}>{primaryCta.label}</Button> : null}
              {secondaryCta ? (
                <Button href={secondaryCta.href} variant="secondary">
                  {secondaryCta.label}
                </Button>
              ) : null}
            </div>
          ) : null}
        </div>
        {children ? <div className="hero-band__aside">{children}</div> : null}
      </div>
    </section>
  );
}
