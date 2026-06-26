import type {
  FAQItem,
  FormField,
  Metric,
  NavItem,
  ProcessStep,
  Sector,
  SourcedText,
  TeamRole,
} from "./types";

export const siteMeta = {
  name: "SunPark",
  description:
    "Turn commercial parking in Morocco into shaded solar power with zero upfront capex.",
  primaryCta: "Get in touch",
  secondaryCta: "How it works",
};

export const navigation: NavItem[] = [
  { label: "Solution", href: "/solution" },
  { label: "Sectors", href: "/sectors" },
  { label: "Process", href: "/process" },
  { label: "Company", href: "/company" },
  { label: "FAQ", href: "/faq" },
  { label: "Contact", href: "/contact" },
];

export const positioning: SourcedText = {
  publicText:
    "SunPark converts existing commercial parking into shaded solar infrastructure. We fund, own, and operate the carport while your site buys clean electricity through a long-term PPA.",
  sourceNotes: [
    {
      document: "Entrepreneurship Doc (1).pdf",
      locator: "Business overview and high-level proposition",
      evidence:
        "SunPark finances, builds, owns and operates modular solar canopies over commercial parking lots; clients pay nothing upfront and sign a 20-year PPA.",
    },
    {
      document: "SunPark_Deck_GBP.pptx (1).pptx",
      locator: "Slides 5-6",
      evidence:
        "Solar Carport as a Service: fund, build, own and run modular solar canopies over commercial parking.",
    },
  ],
};

export const publicMetrics: Metric[] = [
  {
    value: "0",
    label: "Upfront capex",
    context:
      "SunPark carries the installation and ownership burden so customers can start with a commercial energy contract.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 5",
        evidence: "Clients pay zero upfront; SunPark carries the full capex.",
      },
    ],
  },
  {
    value: "GBP 0.069/kWh",
    label: "Source-modelled PPA rate",
    context:
      "The source model sets the PPA rate below the GBP 0.086/kWh commercial grid benchmark.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition",
        evidence:
          "Twenty-year PPAs at GBP 0.069/kWh against a commercial tariff of approximately GBP 0.086/kWh.",
      },
    ],
  },
  {
    value: "1.25M kWh",
    label: "Typical annual generation",
    context:
      "A source-modelled commercial carport can create a meaningful on-site renewable energy supply.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 9",
        evidence: "Base case: approximately 1.25M kWh/year.",
      },
    ],
  },
  {
    value: "< 5 MW",
    label: "Simplified licensing threshold",
    context:
      "Law 82-21 creates a clearer route for distributed self-generation projects below this scale.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition and sector analysis",
        evidence:
          "Law 82-21 established distributed self-generation and simplified licensing for installations below 5 MW.",
      },
    ],
  },
];

export const benefits = [
  {
    title: "Start without upfront capex",
    body: "SunPark funds and owns the carport, so you can start with procurement, not capital expenditure.",
  },
  {
    title: "Lock in lower-cost power",
    body: "You buy generated electricity through a long-term PPA set below the source grid benchmark.",
  },
  {
    title: "Upgrade parking experience",
    body: "Your parking area keeps its core function while adding shade, comfort, and clean generation.",
  },
  {
    title: "Offload operations to SunPark",
    body: "SunPark handles monitoring, maintenance coordination, and long-term operational continuity.",
  },
];

export const howItWorksPreview = [
  {
    title: "Assess the site",
    body: "SunPark reviews the parking area, energy profile, ownership context, and grid pathway before any commercial proposal.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Initial development plan and implementation roadmap",
        evidence:
          "Early phases include feasibility, regulatory preparation, pilot-site commitment, and technical assessment.",
      },
    ],
  },
  {
    title: "Structure the PPA",
    body: "The customer decision is framed as energy procurement: no asset purchase, no upfront capex, and a long-term PPA.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition",
        evidence:
          "SunPark transforms solar adoption from an asset-purchase decision into a long-term energy procurement decision.",
      },
    ],
  },
  {
    title: "Build and connect",
    body: "SunPark coordinates EPC delivery, regulatory engagement, and grid connection work around the approved site plan.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 12",
        evidence:
          "Execution roadmap includes regulatory approvals, ONEE grid sign-off, EPC selection, build, and commissioning.",
      },
    ],
  },
  {
    title: "Operate and monitor",
    body: "Once live, SunPark manages performance, maintenance coordination, and the ongoing energy relationship.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Operational architecture",
        evidence:
          "Operational layers include asset O&M, performance monitoring, and commercial relationship management.",
      },
    ],
  },
];

export const moroccoContext = [
  {
    title: "Energy pressure is structural",
    body: "Morocco imports approximately 90% of its energy, so commercial sites are exposed to wider energy-market pressure.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 3",
        evidence: "Morocco imports 90% of its energy.",
      },
    ],
  },
  {
    title: "Policy has opened the door",
    body: "Law 82-21 creates a framework for distributed self-generation and third-party PPAs, with simplified licensing below 5 MW.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition",
        evidence:
          "Law 82-21 established distributed self-generation under third-party PPAs and simplified licensing below 5 MW.",
      },
    ],
  },
  {
    title: "Commercial solar still needs a simpler model",
    body: "The documents identify financing, ownership, and contractual barriers as the reasons many commercial sites have not adopted solar.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Research and traction sections",
        evidence:
          "Recurring blockers include ROI mismatch, split landlord-tenant ownership, and lack of standardised PPA structures.",
      },
    ],
  },
];

export const solutionModel = [
  {
    title: "SunPark funds the capex",
    body: "The customer does not need to finance the carport as a construction project or place the asset on its own balance sheet.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slides 5 and 8",
        evidence:
          "Clients pay zero upfront; SunPark finances, builds, and owns the carport.",
      },
    ],
  },
  {
    title: "SunPark owns and operates the asset",
    body: "Ownership, performance responsibility, and maintenance coordination sit with SunPark throughout the relationship.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Business overview",
        evidence:
          "SunPark owns the asset, carries the risk, and operates the infrastructure for the contract term.",
      },
    ],
  },
  {
    title: "The customer buys electricity",
    body: "The site buys generated electricity through a PPA priced below the commercial grid benchmark in the source model.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition",
        evidence:
          "Customers buy generated electricity under 20-year PPAs at GBP 0.069/kWh against a GBP 0.086/kWh grid benchmark.",
      },
    ],
  },
];

export const installedSystem = [
  {
    title: "Modular canopy structure",
    body: "A steel-frame carport structure is designed around existing commercial parking rather than new land acquisition.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Detailed solution description",
        evidence: "Technical architecture includes steel-frame modular solar canopy structure.",
      },
    ],
  },
  {
    title: "Solar generation hardware",
    body: "The source architecture uses monocrystalline PV, string inverters, and behind-the-meter grid connection.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Detailed solution description",
        evidence:
          "Technical architecture includes Tier-1 monocrystalline PV, string inverters, and behind-the-meter connection.",
      },
    ],
  },
  {
    title: "Monitoring and EV readiness",
    body: "The system is planned with remote monitoring and EV-charging readiness from the installation stage.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 6",
        evidence:
          "Every carport is EV-ready at install and designed for future charging integration.",
      },
    ],
  },
  {
    title: "Morocco-specific design checks",
    body: "Feasibility work accounts for conditions such as dust, thermal performance, and wind loads.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Detailed solution description",
        evidence:
          "Morocco-specific considerations include dust mitigation, thermal performance, and wind loads.",
      },
    ],
  },
];

export const customerOutcomes = [
  {
    title: "Generate cleaner electricity on site",
    body: "Your parking footprint becomes a practical renewable energy source for day-to-day operations.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition",
        evidence:
          "SunPark sells generated electricity directly to site hosts from modular solar canopies.",
      },
    ],
  },
  {
    title: "Keep the commercial decision simple",
    body: "Your team evaluates an energy contract, not a construction project with ownership complexity.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 11",
        evidence: "Solar becomes a simple commercial decision, not a complex infrastructure project.",
      },
    ],
  },
  {
    title: "Get long-term service continuity",
    body: "SunPark stays responsible for operation, monitoring, and maintenance coordination after commissioning.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Operational architecture",
        evidence:
          "Operations include asset O&M, performance monitoring, and commercial relationship management.",
      },
    ],
  },
];

export const sunparkResponsibilities = [
  {
    title: "Feasibility and system design",
    body: "Assess site suitability, size the system, and define technical requirements for the carport.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Implementation plan",
        evidence:
          "Phase 3 includes feasibility studies, EPC contractor selection, and first project SPV establishment.",
      },
    ],
  },
  {
    title: "PPA and regulatory coordination",
    body: "Coordinate the commercial PPA structure and regulatory pathway under Law 82-21.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Implementation roadmap",
        evidence:
          "Regulatory preparation includes ONEE consultation, required documentation under Law 82-21, and standardised PPA framework development.",
      },
    ],
  },
  {
    title: "EPC oversight and operations",
    body: "Select and oversee delivery partners, then manage performance and service after launch.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Implementation and operational architecture",
        evidence:
          "Akilesh leads EPC oversight; operations include O&M, monitoring, and customer relationship.",
      },
    ],
  },
];

export const multiSiteExpansion = [
  {
    title: "One framework",
    body: "A standardised commercial structure reduces repeated negotiation as a customer considers more sites.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 11",
        evidence: "One negotiation becomes a rollout under a single framework.",
      },
    ],
  },
  {
    title: "Repeatable delivery",
    body: "The model is designed around repeatable feasibility, PPA, EPC, and operations workflows.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Implementation roadmap",
        evidence:
          "The roadmap focuses on contractual, regulatory, and financing foundations required for repeatable portfolio expansion.",
      },
    ],
  },
  {
    title: "Simple repeat decisions",
    body: "Future sites can be evaluated through the same energy-service structure instead of restarting from zero.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level overview",
        evidence:
          "Reference-led expansion creates a pathway to subsequent deployments across a customer's wider property portfolio.",
      },
    ],
  },
];

export const processResponsibilities = [
  {
    title: "SunPark handles",
    body: "Feasibility, system design, commercial PPA structuring, regulatory coordination, EPC oversight, and long-term performance management.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Implementation plan and team architecture",
        evidence:
          "The implementation roadmap covers legal, regulatory, feasibility, EPC, construction, commissioning and operations workstreams.",
      },
    ],
  },
  {
    title: "The customer supports",
    body: "Site access, basic property information, energy-use context, and commercial review of the PPA proposal.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Solution and customer journey sections",
        evidence:
          "The model requires site host participation in feasibility and PPA contracting while SunPark carries asset ownership and operations.",
      },
    ],
  },
  {
    title: "Specialists support",
    body: "Legal, engineering, finance, and tax specialists are brought in where execution quality is critical.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Advisor and specialist support",
        evidence:
          "Moroccan legal counsel, engineering, tax, and project finance advisors support specialist execution areas.",
      },
    ],
  },
];

export const regulatorySupport = [
  {
    title: "Law 82-21 framework",
    body: "SunPark works within the distributed self-generation and third-party PPA framework created by Law 82-21.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Regulatory environment",
        evidence:
          "Law 82-21 represents the legal framework for distributed self-generation under third-party PPAs.",
      },
    ],
  },
  {
    title: "Grid coordination",
    body: "The process includes ONEE-related grid coordination, with timing treated as an execution dependency rather than a guaranteed date.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Implementation roadmap and critical risks",
        evidence:
          "ONEE consultation, grid sign-off and regulatory timelines are identified as important dependencies and risks.",
      },
    ],
  },
  {
    title: "Below 5 MW pathway",
    body: "The source documents identify simplified licensing for installations below 5 MW as a practical enabler for commercial projects.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition",
        evidence:
          "Installations below 5 MW benefit from simplified licensing procedures.",
      },
    ],
  },
];

export const operationsAfterLaunch = [
  {
    title: "Performance monitoring",
    body: "SunPark tracks system performance so the carport remains an operating energy asset, not a one-time installation.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Operational architecture",
        evidence:
          "Operational architecture includes performance monitoring and remote monitoring/SCADA.",
      },
    ],
  },
  {
    title: "Maintenance coordination",
    body: "Operations include maintenance coordination and asset-management responsibility over the life of the PPA.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Operational architecture",
        evidence:
          "Operations include asset O&M and performance monitoring.",
      },
    ],
  },
  {
    title: "Commercial relationship",
    body: "The ongoing relationship is managed as an energy service, including billing and customer performance communication.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Operational architecture",
        evidence:
          "Customer experience includes monthly billing, real-time dashboard, and annual sustainability reporting.",
      },
    ],
  },
];

export const operatingPrinciples = [
  {
    title: "Customer simplicity",
    body: "Solar should feel like a clear commercial energy decision, not a complex infrastructure project.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 11",
        evidence:
          "Solar becomes a simple commercial decision, not a complex infrastructure project.",
      },
    ],
  },
  {
    title: "Asset-grade discipline",
    body: "The company is structured around the technical, financial, regulatory, and commercial disciplines needed for infrastructure work.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Team architecture",
        evidence:
          "Infrastructure businesses depend on coordinated execution of technical, financial, regulatory, and commercial activities.",
      },
    ],
  },
  {
    title: "Local regulatory understanding",
    body: "The model is built around Morocco's Law 82-21 environment and the practical realities of grid coordination.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Regulatory environment",
        evidence:
          "Law 82-21 and ONEE coordination are central to SunPark's regulatory and implementation approach.",
      },
    ],
  },
  {
    title: "Long-term service mindset",
    body: "SunPark remains involved after installation through monitoring, operations, and customer relationship management.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Operational architecture",
        evidence:
          "Operational architecture includes asset O&M, performance monitoring and commercial relationship management.",
      },
    ],
  },
];

export const specialistSupport = [
  {
    title: "Moroccan legal counsel",
    body: "Supports regulatory filings and PPA development.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Advisor and specialist support",
        evidence:
          "Moroccan legal counsel supports regulatory filings and PPA development.",
      },
    ],
  },
  {
    title: "Engineering support",
    body: "Provides specialist input where technical design, procurement, and delivery quality matter.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Advisor and specialist support",
        evidence:
          "Engineering advisors provide expertise in specialist execution areas.",
      },
    ],
  },
  {
    title: "Project finance and tax support",
    body: "Adds specialist capability for finance structuring and tax considerations without implying a large fixed-cost team.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Advisor and specialist support",
        evidence:
          "Tax and project finance advisors provide expertise without imposing full-time fixed costs.",
      },
    ],
  },
];

export const ppaExplainers = [
  {
    title: "What is a PPA?",
    body: "A Power Purchase Agreement is the commercial contract through which the site buys the electricity generated by the carport, instead of buying the infrastructure itself.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition",
        evidence:
          "Customers buy generated electricity under twenty-year PPAs rather than owning the solar asset.",
      },
    ],
  },
  {
    title: "What is Solar Carport as a Service?",
    body: "It is SunPark's service model: finance, build, own, operate, and maintain solar canopies over commercial parking while the customer buys the generated electricity.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 5",
        evidence:
          "Solar Carport as a Service: fund, build, own and run modular solar canopies over commercial parking.",
      },
    ],
  },
  {
    title: "Why parking areas?",
    body: "Parking areas are already developed surfaces. A canopy can keep the parking function while adding shade and electricity generation.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slides 5-6",
        evidence:
          "Built over existing parking; no land acquisition; carparks gain a second job generating power.",
      },
    ],
  },
];

export const sectors: Sector[] = [
  {
    name: "Retail",
    headline: "Lower operating costs and shaded customer parking.",
    body: "Retail sites can use parking areas to support energy procurement without asking customers or landlords to manage solar ownership.",
    suitability: ["Customer parking", "Multi-site rollout potential", "Visible sustainability"],
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Market and go-to-market sections",
        evidence:
          "SunPark targets retail, logistics, hospitality, and office sectors; retail is a primary commercial segment.",
      },
    ],
  },
  {
    name: "Logistics",
    headline: "Large paved areas with practical energy demand.",
    body: "Logistics properties often have parking or yard surfaces that can host solar canopies while keeping operations moving.",
    suitability: ["Large parking areas", "Operational energy use", "Practical feasibility pathway"],
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Target segments and pilot discussion",
        evidence:
          "Logistics is included in target sectors and the first validation route is a logistics warehouse.",
      },
    ],
  },
  {
    name: "Hospitality",
    headline: "Guest comfort paired with cleaner electricity.",
    body: "Hotels and hospitality venues can turn parking shade into a visible sustainability and cost-reduction asset.",
    suitability: ["Guest parking", "Visible sustainability", "Energy cost pressure"],
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Market sizing and segmentation",
        evidence: "Hospitality is included in SunPark's target commercial sectors.",
      },
    ],
  },
  {
    name: "Offices",
    headline: "Employee parking that supports the building's energy strategy.",
    body: "Office properties can use parking areas to add on-site renewable generation without turning solar into an ownership project.",
    suitability: ["Employee parking", "ESG reporting support", "Long-term operating-cost focus"],
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Market sizing and segmentation",
        evidence: "Office properties are included in SunPark's target commercial sectors.",
      },
    ],
  },
];

export const processSteps: ProcessStep[] = [
  {
    title: "Site review",
    body: "SunPark starts by understanding the parking area, building load, ownership context, and project fit.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Implementation and technical feasibility sections",
        evidence: "Feasibility studies and pilot-site commitment are part of the early execution path.",
      },
    ],
  },
  {
    title: "Feasibility and sizing",
    body: "The system is sized around parking geometry, energy demand, grid proximity, and Morocco-specific site conditions.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Technical architecture",
        evidence:
          "Technical assumptions include modular carports, PV sizing, behind-the-meter connection, heat, dust, and wind loads.",
      },
    ],
  },
  {
    title: "Commercial proposal and PPA",
    body: "The customer receives a PPA-led proposal, keeping the decision focused on energy procurement rather than asset purchase.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Solution and business model sections",
        evidence:
          "The model transforms solar adoption from an asset-purchase decision into a long-term energy procurement decision.",
      },
    ],
  },
  {
    title: "Regulatory and grid coordination",
    body: "SunPark coordinates the regulatory and grid pathway under the Law 82-21 framework without promising guaranteed approval timing.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Regulatory and implementation sections",
        evidence:
          "Law 82-21 and ONEE coordination are core execution workstreams; regulatory timelines remain an execution risk.",
      },
    ],
  },
  {
    title: "EPC delivery",
    body: "Experienced EPC delivery partners are selected and overseen against the required technical and performance standards.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Implementation plan",
        evidence:
          "Delivery risk is mitigated through experienced EPC contractors and performance-based arrangements.",
      },
    ],
  },
  {
    title: "Commissioning",
    body: "The carport is connected, commissioned, and prepared for long-term operation under the PPA.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 12",
        evidence: "Execution roadmap includes build and commissioning before scale.",
      },
    ],
  },
  {
    title: "Monitoring and service",
    body: "After launch, SunPark manages performance, maintenance coordination, and the ongoing commercial relationship.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Operational architecture",
        evidence:
          "Operations include asset O&M, performance monitoring, commercial relationship, dashboard, and reporting.",
      },
    ],
  },
];

export const teamRoles: TeamRole[] = [
  {
    name: "Youssef",
    role: "Commercial & PPA",
    responsibility: "Commercial access, site-owner relationships, and PPA negotiations.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 14",
        evidence: "Youssef owns Morocco commercial access, retailer relationships and PPA negotiations.",
      },
    ],
  },
  {
    name: "Fariha",
    role: "Finance & Capital",
    responsibility: "Financial model, capital structure, and SPV architecture.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 14",
        evidence: "Fariha owns the financial model, capital structure and SPV architecture.",
      },
    ],
  },
  {
    name: "Akilesh",
    role: "Technical & EPC",
    responsibility: "Technical feasibility, system sizing, EPC selection, and delivery quality.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 14",
        evidence: "Akilesh owns technical feasibility, system sizing, EPC selection and delivery quality.",
      },
    ],
  },
  {
    name: "Sybil",
    role: "Ops & Regulatory",
    responsibility: "Operations, regulation, and stakeholder coordination across rollout.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 14",
        evidence: "Sybil owns operations, regulation and stakeholder coordination.",
      },
    ],
  },
  {
    name: "Ahmad",
    role: "Partnerships",
    responsibility: "Partnerships, investor access, and regional expansion mapping.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 14",
        evidence: "Ahmad owns partnerships, investor access and regional expansion mapping.",
      },
    ],
  },
];

export const faqItems: FAQItem[] = [
  {
    question: "Who owns the solar carport?",
    answer:
      "SunPark owns the asset. The customer does not buy the carport; they buy the electricity it generates through a long-term PPA.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "Business overview",
        evidence: "SunPark owns the asset, carries the risk, and collects revenue through the contract term.",
      },
    ],
  },
  {
    question: "What does the customer pay upfront?",
    answer:
      "The customer pays no upfront capex in the source model. SunPark finances the installation and keeps the customer decision focused on energy procurement.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 5",
        evidence: "GBP 0 upfront for the client.",
      },
    ],
  },
  {
    question: "How is the electricity price set?",
    answer:
      "The source model sets the PPA rate below the commercial grid benchmark, with the customer buying generated electricity per kWh under the PPA.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition",
        evidence: "PPA tariff of GBP 0.069/kWh compared with grid benchmark of GBP 0.086/kWh.",
      },
    ],
  },
  {
    question: "Does this require new land?",
    answer:
      "No new land is required for the core model. The carport is designed over existing commercial parking areas.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 6",
        evidence: "Built over existing parking; no land acquisition.",
      },
    ],
  },
  {
    question: "Can EV charging be added later?",
    answer:
      "The source design frames every carport as EV-charging ready, so future charging integration can be planned from the installation stage.",
    sourceNotes: [
      {
        document: "SunPark_Deck_GBP.pptx (1).pptx",
        locator: "Slide 6",
        evidence: "Every carport is EV-ready at install and designed for future charging integration.",
      },
    ],
  },
  {
    question: "What regulations make this possible?",
    answer:
      "Law 82-21 created a framework for distributed self-generation and third-party PPAs, with simplified licensing for installations below 5 MW.",
    sourceNotes: [
      {
        document: "Entrepreneurship Doc (1).pdf",
        locator: "High-level proposition and regulatory environment",
        evidence: "Law 82-21 established the legal framework for distributed self-generation and PPAs.",
      },
    ],
  },
];

export const contactFields: FormField[] = [
  { name: "name", label: "Name", type: "text", required: true },
  { name: "company", label: "Company", type: "text", required: true },
  { name: "email", label: "Email", type: "email", required: true },
  { name: "phone", label: "Phone", type: "tel" },
  { name: "city", label: "City", type: "text" },
  {
    name: "siteType",
    label: "Site type",
    type: "select",
    options: ["Retail", "Logistics", "Hospitality", "Office", "Other"],
  },
  { name: "parkingSpaces", label: "Approximate parking spaces", type: "text" },
  {
    name: "interest",
    label: "Current interest",
    type: "select",
    options: ["Feasibility", "PPA", "Partnership", "Financing", "EPC/advisory"],
  },
  { name: "message", label: "Message", type: "textarea" },
];
