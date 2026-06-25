import Link from "next/link";
import { navigation, positioning, siteMeta } from "@/content/site";
import { Button } from "./Button";

export function Footer() {
  return (
    <footer className="footer-shell">
      <div className="footer">
        <div className="footer__intro">
          <Link className="footer__brand" href="/">
            SunPark
          </Link>
          <p className="footer__copy">{positioning.publicText}</p>
        </div>

        <nav aria-label="Footer navigation" className="footer__links">
          {navigation.map((item) => (
            <Link className="footer__link" href={item.href} key={item.href}>
              {item.label}
            </Link>
          ))}
        </nav>

        <div className="footer__cta">
          <p className="type-caption">Commercial parking assets in Morocco.</p>
          <Button href="/contact">{siteMeta.primaryCta}</Button>
        </div>
      </div>
    </footer>
  );
}
