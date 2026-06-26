"use client";

import Link from "next/link";
import Image from "next/image";
import { useState } from "react";
import { navigation, siteMeta } from "@/content/site";
import { Button } from "./Button";

export function TopNav() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="top-nav-shell">
      <div className="top-nav">
        <Link
          aria-label="SunPark home"
          className="top-nav__brand"
          href="/"
          onClick={() => setIsOpen(false)}
        >
          <Image
            src="/logo.png"
            alt="SunPark"
            height={36}
            width={108}
            style={{ height: 36, width: "auto", display: "block", mixBlendMode: "multiply" }}
            priority
          />
        </Link>

        <nav aria-label="Primary navigation" className="top-nav__links">
          {navigation.map((item) => (
            <Link className="top-nav__link" href={item.href} key={item.href}>
              {item.label}
            </Link>
          ))}
        </nav>

        <div className="top-nav__actions">
          <Button href="/contact" variant="secondary">Contact us</Button>
        </div>

        <button
          aria-controls="mobile-navigation"
          aria-expanded={isOpen}
          aria-label="Toggle navigation"
          className="top-nav__toggle"
          onClick={() => setIsOpen((current) => !current)}
          type="button"
        >
          <span />
          <span />
        </button>
      </div>

      <div
        className="mobile-nav"
        data-open={isOpen ? "true" : "false"}
        id="mobile-navigation"
      >
        <nav aria-label="Mobile navigation" className="mobile-nav__links">
          {navigation.map((item) => (
            <Link
              className="mobile-nav__link"
              href={item.href}
              key={item.href}
              onClick={() => setIsOpen(false)}
            >
              {item.label}
            </Link>
          ))}
          <Button href="/contact" variant="secondary" onClick={() => setIsOpen(false)}>
            Contact us
          </Button>
        </nav>
      </div>
    </header>
  );
}
