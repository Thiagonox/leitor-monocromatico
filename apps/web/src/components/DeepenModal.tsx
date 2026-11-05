'use client';

import React, { useState, useEffect, useRef } from 'react';
import {
  X,
  Sparkles,
  Loader2,
  Send,
  GraduationCap,
  Zap,
  Coffee,
  ShieldAlert,
  Bot,
  User,
  CornerDownLeft,
} from 'lucide-react';
import { sendAgentChatMessage } from '@/lib/api';
import { AGENT_LIST, AGENT_PERSONAS, AgentId, AgentPersona } from '@mono-reader/shared';

interface DeepenModalProps {
  isOpen: boolean;
  onClose: () => void;
  initialTopic?: string;
  contextText?: string;
}

interface ChatItem {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  agentId?: AgentId;
  createdAt: string;
}

export function DeepenModal({
  isOpen,
  onClose,
  initialTopic = '',
  contextText = '',
}: DeepenModalProps) {
  const [selectedAgentId, setSelectedAgentId] = useState<AgentId>('curseiro');
  const [messages, setMessages] = useState<ChatItem[]>([]);
  const [inputMessage, setInputMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const messagesEndRef = useRef<HTMLDivElement | null>(null);
  const activeAgent = AGENT_PERSONAS[selectedAgentId] || AGENT_PERSONAS.curseiro;

  // Rola para a mensagem mais recente
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  // Inicializa o chat quando o modal abre
  useEffect(() => {
    if (!isOpen) {
      setMessages([]);
      setInputMessage('');
      setError(null);
      return;
    }

    const currentAgent = AGENT_PERSONAS[selectedAgentId];

    // Se veio um termo/conceito selecionado pelo leitor, inicia o chat com esse pedido
    if (initialTopic && initialTopic.trim()) {
      const topicClean = initialTopic.trim();
      const initialUserPrompt = `Como você explica o conceito de "${topicClean}" no contexto desta leitura?`;

      setMessages([
        {
          id: 'user-init',
          role: 'user',
          content: initialUserPrompt,
          createdAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        },
      ]);

      setLoading(true);
      sendAgentChatMessage({
        messages: [{ role: 'user', content: initialUserPrompt }],
        agentId: selectedAgentId,
        topic: topicClean,
        contextText,
      })
        .then((res) => {
          setMessages((prev) => [
            ...prev,
            {
              id: 'agent-init',
              role: 'assistant',
              content: res.message.content,
              agentId: selectedAgentId,
              createdAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
            },
          ]);
        })
        .catch((err) => {
          setError(err.message || 'Erro ao consultar o agente.');
        })
        .finally(() => {
          setLoading(false);
        });
    } else {
      // Saudação personalizada do agente
      setMessages([
        {
          id: `greet-${selectedAgentId}`,
          role: 'assistant',
          content: currentAgent.greeting,
          agentId: selectedAgentId,
          createdAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        },
      ]);
    }
  }, [isOpen, initialTopic, contextText]);

  // Se trocar de agente durante o chat, envia uma mensagem de entrada do novo agente
  const handleSwitchAgent = (newAgentId: AgentId) => {
    if (newAgentId === selectedAgentId) return;
    setSelectedAgentId(newAgentId);
    const newAgent = AGENT_PERSONAS[newAgentId];

    setMessages((prev) => [
      ...prev,
      {
        id: `switch-${Date.now()}`,
        role: 'assistant',
        content: `*${newAgent.name} (${newAgent.badge}) entrou na conversa.* "${newAgent.tagline}"`,
        agentId: newAgentId,
        createdAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      },
    ]);
  };

  const handleSendMessage = async (textToSend?: string) => {
    const text = (textToSend || inputMessage).trim();
    if (!text || loading) return;

    const userMsg: ChatItem = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: text,
      createdAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    const newHistory = [...messages, userMsg];
    setMessages(newHistory);
    setInputMessage('');
    setLoading(true);
    setError(null);

    try {
      const payloadMessages = newHistory.map((m) => ({
        role: m.role,
        content: m.content,
      }));

      const res = await sendAgentChatMessage({
        messages: payloadMessages,
        agentId: selectedAgentId,
        topic: initialTopic,
        contextText,
      });

      const assistantMsg: ChatItem = {
        id: `assistant-${Date.now()}`,
        role: 'assistant',
        content: res.message.content,
        agentId: selectedAgentId,
        createdAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      setMessages((prev) => [...prev, assistantMsg]);
    } catch (err: any) {
      setError(err?.message || 'Falha ao responder. Tente novamente.');
    } finally {
      setLoading(false);
    }
  };

  const getAgentIcon = (id: AgentId) => {
    switch (id) {
      case 'professor':
        return <GraduationCap className="w-4 h-4" />;
      case 'curseiro':
        return <Zap className="w-4 h-4" />;
      case 'simplificador':
        return <Coffee className="w-4 h-4" />;
      case 'corretor':
        return <ShieldAlert className="w-4 h-4" />;
      default:
        return <Bot className="w-4 h-4" />;
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-black/70 backdrop-blur-sm" onClick={onClose} />

      {/* Janela de Chat com Agentes */}
      <div className="relative w-full max-w-2xl bg-[var(--bg-primary)] border border-[var(--border-strong)] rounded-lg shadow-2xl z-10 h-[88vh] sm:h-[80vh] flex flex-col overflow-hidden font-sans text-[var(--text-primary)]">
        {/* Cabeçalho do Chat */}
        <div className="p-3 sm:p-4 border-b border-[var(--border-color)] bg-[var(--bg-surface)] flex items-center justify-between gap-2 shrink-0">
          <div className="flex items-center gap-2">
            <span className="p-1.5 rounded border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)]">
              {getAgentIcon(selectedAgentId)}
            </span>
            <div>
              <div className="flex items-center gap-2">
                <h3 className="font-serif text-sm sm:text-base font-bold">
                  {activeAgent.name}
                </h3>
                <span className="text-[10px] font-mono px-1.5 py-0.2 rounded border border-[var(--border-color)] bg-[var(--bg-secondary)] text-[var(--text-secondary)]">
                  {activeAgent.badge}
                </span>
              </div>
              <p className="text-[11px] font-mono text-[var(--text-muted)] line-clamp-1">
                {activeAgent.role}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 rounded hover:bg-[var(--bg-secondary)] text-[var(--text-muted)] hover:text-[var(--text-primary)] transition-colors"
            title="Fechar chat com agentes"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Seletor de Agentes (Tabs de Personalidade) */}
        <div className="px-3 sm:px-4 py-2 border-b border-[var(--border-color)] bg-[var(--bg-secondary)]/50 flex items-center gap-1.5 overflow-x-auto no-scrollbar shrink-0">
          <span className="text-[10px] font-mono text-[var(--text-muted)] uppercase shrink-0 mr-1">
            Agente:
          </span>
          {AGENT_LIST.map((agent: AgentPersona) => {
            const isSelected = agent.id === selectedAgentId;
            return (
              <button
                key={agent.id}
                onClick={() => handleSwitchAgent(agent.id)}
                className={`flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-mono transition-all shrink-0 ${
                  isSelected
                    ? 'bg-[var(--text-primary)] text-[var(--bg-primary)] font-bold shadow-sm'
                    : 'border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-secondary)] hover:bg-[var(--bg-secondary)]'
                }`}
                title={agent.description}
              >
                {getAgentIcon(agent.id)}
                <span>{agent.name}</span>
              </button>
            );
          })}
        </div>

        {/* Notificação de Contexto de Leitura */}
        {(initialTopic || contextText) && (
          <div className="px-4 py-1.5 bg-[var(--bg-card)] border-b border-[var(--border-color)] flex items-center justify-between text-[11px] font-mono text-[var(--text-muted)] shrink-0">
            <span className="truncate flex-1 mr-2">
              📖 Contexto: <strong className="text-[var(--text-primary)]">{initialTopic || 'Trecho do Capítulo'}</strong>
            </span>
            <span className="text-[10px] opacity-75 hidden sm:inline">IA contextualizada</span>
          </div>
        )}

        {/* Área de Mensagens com Scroll */}
        <div className="flex-1 overflow-y-auto p-3 sm:p-4 space-y-4">
          {messages.map((msg) => {
            const isUser = msg.role === 'user';
            const agentOfMsg = msg.agentId ? AGENT_PERSONAS[msg.agentId] : activeAgent;

            if (isUser) {
              return (
                <div key={msg.id} className="flex justify-end items-end gap-2">
                  <div className="max-w-[85%] sm:max-w-[75%] rounded-lg px-3 py-2 bg-[var(--text-primary)] text-[var(--bg-primary)] text-xs sm:text-sm font-sans shadow-sm">
                    <p className="whitespace-pre-line leading-relaxed">{msg.content}</p>
                    <span className="block text-[9px] font-mono opacity-60 text-right mt-1">
                      {msg.createdAt}
                    </span>
                  </div>
                </div>
              );
            }

            return (
              <div key={msg.id} className="flex justify-start items-start gap-2.5">
                <div className="w-7 h-7 rounded-full border border-[var(--border-strong)] bg-[var(--bg-surface)] flex items-center justify-center shrink-0 text-[var(--text-primary)] mt-0.5 shadow-sm">
                  {msg.agentId ? getAgentIcon(msg.agentId) : <Bot className="w-3.5 h-3.5" />}
                </div>

                <div className="max-w-[90%] sm:max-w-[85%] rounded-lg border border-[var(--border-color)] bg-[var(--bg-card)] p-3 sm:p-4 text-xs sm:text-sm shadow-sm">
                  <div className="flex items-center justify-between border-b border-[var(--border-color)]/60 pb-1.5 mb-2 font-mono text-[11px]">
                    <span className="font-bold text-[var(--text-primary)] flex items-center gap-1.5">
                      {agentOfMsg.name}
                      <span className="text-[9px] font-normal px-1 py-0.2 rounded border border-[var(--border-color)] text-[var(--text-muted)]">
                        {agentOfMsg.badge}
                      </span>
                    </span>
                    <span className="text-[9px] text-[var(--text-muted)]">{msg.createdAt}</span>
                  </div>

                  <div className="font-serif leading-relaxed text-[var(--text-primary)] whitespace-pre-line">
                    {msg.content}
                  </div>
                </div>
              </div>
            );
          })}

          {loading && (
            <div className="flex items-center gap-2 text-xs font-mono text-[var(--text-muted)] py-2">
              <Loader2 className="w-4 h-4 animate-spin text-[var(--text-primary)]" />
              <span>{activeAgent.name} está formulando a resposta...</span>
            </div>
          )}

          {error && (
            <div className="p-3 rounded border border-red-500/40 bg-red-950/20 text-red-400 text-xs font-mono">
              {error}
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Sugestões Rápidas de Perguntas (Pills) */}
        <div className="px-3 sm:px-4 py-1.5 border-t border-[var(--border-color)] bg-[var(--bg-surface)] flex items-center gap-1.5 overflow-x-auto no-scrollbar shrink-0">
          <span className="text-[10px] font-mono text-[var(--text-muted)] uppercase shrink-0">
            Sugestões:
          </span>
          {activeAgent.quickPrompts.map((promptText, pIdx) => (
            <button
              key={pIdx}
              onClick={() => handleSendMessage(promptText)}
              disabled={loading}
              className="text-[11px] font-mono px-2.5 py-1 rounded-full border border-[var(--border-color)] bg-[var(--bg-secondary)] hover:bg-[var(--border-color)] text-[var(--text-primary)] transition-colors whitespace-nowrap shrink-0 disabled:opacity-50"
            >
              {promptText}
            </button>
          ))}
        </div>

        {/* Barra de Entrada de Mensagem */}
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSendMessage();
          }}
          className="p-3 border-t border-[var(--border-strong)] bg-[var(--bg-primary)] flex items-center gap-2 shrink-0"
        >
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            placeholder={`Pergunte ao ${activeAgent.name}...`}
            disabled={loading}
            className="flex-1 p-2 sm:p-2.5 rounded border border-[var(--border-color)] bg-[var(--bg-surface)] text-[var(--text-primary)] text-xs sm:text-sm font-sans focus:outline-none focus:border-[var(--border-strong)]"
          />

          <button
            type="submit"
            disabled={loading || !inputMessage.trim()}
            className="px-3.5 py-2 sm:py-2.5 rounded border border-[var(--border-strong)] bg-[var(--text-primary)] text-[var(--bg-primary)] font-mono text-xs font-bold hover:opacity-90 disabled:opacity-40 flex items-center gap-1 transition-opacity shrink-0"
            title="Enviar mensagem"
          >
            {loading ? (
              <Loader2 className="w-4 h-4 animate-spin" />
            ) : (
              <>
                <Send className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Enviar</span>
              </>
            )}
          </button>
        </form>
      </div>
    </div>
  );
}
